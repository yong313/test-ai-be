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
        
        for generation in llm._stream([HumanMessage(content=user_input)], callbacks=callbacks):
            content = generation.message.content
            print(f"Generated Token: {content}")
            yield f"0: {json.dumps(content)}\n"
            await asyncio.sleep(0.1)

    return StreamingResponse(generate(), media_type="text/event-stream", headers={"x-vercel-ai-data-stream": "v1"})
# source venv/bin/activate 
# uvicorn main:app --reload
