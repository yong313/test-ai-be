import os
import json
import asyncio
import random
from typing import Any, Dict, List, Optional, Iterator
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
from dotenv import load_dotenv
from langchain.schema.messages import HumanMessage
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chat_models.base import BaseChatModel
from langchain.schema.output import ChatGeneration

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# class CustomGeminiChatModel(BaseChatModel):
#     model_name: str = "gemini-pro"

#     @property
#     def _llm_type(self) -> str:
#         return "custom-gemini"

#     def _generate(self, messages: List[HumanMessage], stop: Optional[List[str]] = None, **kwargs: Any):
#         raise NotImplementedError("Synchronous generation is not implemented. Use _stream instead.")

    # def _stream(self, messages: List[HumanMessage], stop: Optional[List[str]] = None, **kwargs: Any) -> Iterator[ChatGeneration]:
    #     user_input = messages[-1].content
    #     model = genai.GenerativeModel(self.model_name)
    #     response = model.generate_content(user_input, stream=True)

    #     for chunk in response:
    #         if chunk.text:
    #             yield ChatGeneration(message=HumanMessage(content=chunk.text))
    # def _stream(self, messages: List[HumanMessage], stop: Optional[List[str]] = None, **kwargs: Any) -> Iterator[ChatGeneration]:
    #     user_input = messages[-1].content
    #     model = genai.GenerativeModel(self.model_name)
    #     response = model.generate_content(user_input, stream=True)

    #     for chunk in response:
    #         if chunk.text:
    #             # Split the chunk into smaller pieces for smoother streaming
    #             for piece in self._split_text(chunk.text, max_length=10):  # Split into 20-character chunks
    #                 yield ChatGeneration(message=HumanMessage(content=piece))

    # def _split_text(self, text: str, max_length: int) -> List[str]:
    #     """Split text into smaller chunks."""
    #     return [text[i:i + max_length] for i in range(0, len(text), max_length)]


class CustomGeminiChatModel(BaseChatModel):
    model_name: str = "gemini-pro"

    @property
    def _llm_type(self) -> str:
        return "custom-gemini"

    def _generate(self, messages: List[HumanMessage], stop: Optional[List[str]] = None, **kwargs: Any):
        # 명시적으로 동기화 생성을 막음
        raise NotImplementedError("Synchronous generation is not implemented. Use _stream instead.")

    def _stream(self, messages: List[HumanMessage], stop: Optional[List[str]] = None, **kwargs: Any) -> Iterator[ChatGeneration]:
        user_input = messages[-1].content
        model = genai.GenerativeModel(self.model_name)
        response = model.generate_content(user_input, stream=True)

        for chunk in response:
            # finish_reason 검사
            if getattr(chunk, "finish_reason", None) in [3, 4]:
                print(f"Skipping chunk due to finish_reason: {chunk.finish_reason}")
                continue
            if chunk.text:
                for piece in self._split_text(chunk.text, max_length=10):
                    yield ChatGeneration(message=HumanMessage(content=piece))

    def _split_text(self, text: str, max_length: int) -> List[str]:
        """Split text into smaller chunks."""
        return [text[i:i + max_length] for i in range(0, len(text), max_length)]




llm = CustomGeminiChatModel()


@app.post("/chat")
async def chat_completions(request: Request):
    data = await request.json()
    messages = data.get("messages", [])
    if not messages or "content" not in messages[-1]:
        return {"error": "Invalid request format"}

    user_input = messages[-1]["content"]
    print(f"Received User Input: {user_input}")

    async def generate():
        callbacks = [StreamingStdOutCallbackHandler()]  
        messages = ["질문 확인 중입니다.", "데이터베이스 정보를 추출 중입니다.", "관련 문서에서 정보를 추출 중입니다."]
        message_index = 0 
        counter = 0

        # for i in range(9):
        #     if counter == 3:
        #         message_index = (message_index + 1) % len(messages)
        #         counter = 0  

        #     status_message = {"content": messages[message_index]}
        #     print(f"2: {status_message}")
        #     yield f"2: [{json.dumps(status_message)}]\n"

        #     counter += 1 
        #     await asyncio.sleep(1)
            
        # def generate_temperature_data(month: str, weeks: int):
        #     chart_data = []
        #     for i in range(1, weeks + 1):
        #         average_temp = round(random.uniform(-5, 5), 1) 
        #         high_temp = round(average_temp + random.uniform(0, 5), 1)
        #         low_temp = round(average_temp - random.uniform(0, 5), 1)
        #         chart_data.append({
        #             "week": f"Week {i}",
        #             "month": month,
        #             "average_temp": average_temp,
        #             "high_temp": high_temp,
        #             "low_temp": low_temp,
        #         })
        #     return chart_data
        
        # combined_data = []
        # if "12월" in user_input or "11월" in user_input:
        #     november_data = generate_temperature_data("November", 4)
        #     december_data = generate_temperature_data("December", 4)
        #     combined_data = november_data + december_data
        #     print(f"Generated Temperature Data: {combined_data}")


        # if combined_data:
        #     yield f"8: {json.dumps(combined_data)}\n"
        
        for generation in llm._stream([HumanMessage(content=user_input)], callbacks=callbacks):
            content = generation.message.content
            print(f"Generated Token: {content}")
            yield f"0: {json.dumps(content)}\n"
            await asyncio.sleep(0.1)

    return StreamingResponse(generate(), media_type="text/event-stream", headers={"x-vercel-ai-data-stream": "v1"})
# source venv/bin/activate 
# uvicorn main:app --reload
