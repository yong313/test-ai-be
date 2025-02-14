import os
from typing import Any, List, Optional, Iterator
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import google.generativeai as genai
from langchain.schema.messages import HumanMessage
from langchain.chat_models.base import BaseChatModel
from langchain.schema.output import ChatGeneration
from apex import apex_router
from plotly import plotly_router
from chartjs import chartjs_router

# 환경 변수 로드
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# FastAPI 앱 생성 및 CORS 설정
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom Gemini Chat Model 정의
class CustomGeminiChatModel(BaseChatModel):
    model_name: str = "gemini-pro"

    @property
    def _llm_type(self) -> str:
        return "custom-gemini"

    def _generate(self, messages: List[HumanMessage], stop: Optional[List[str]] = None, **kwargs: Any):
        raise NotImplementedError("Synchronous generation is not implemented. Use _stream instead.")

    def _stream(self, messages: List[HumanMessage], stop: Optional[List[str]] = None, **kwargs: Any) -> Iterator[ChatGeneration]:
        user_input = messages[-1].content
        model = genai.GenerativeModel(self.model_name)
        response = model.generate_content(user_input, stream=True)

        for chunk in response:
            if getattr(chunk, "finish_reason", None) in [3, 4]:
                print(f"Skipping chunk due to finish_reason: {chunk.finish_reason}")
                continue
            if chunk.text:
                yield ChatGeneration(message=HumanMessage(content=chunk.text))

llm = CustomGeminiChatModel()


app.include_router(apex_router, prefix="/apex", tags=["ApexCharts"])
app.include_router(plotly_router, prefix="/plotly", tags=["Plotly"])
app.include_router(chartjs_router, prefix="/chartjs", tags=["ChartJs"])



# source venv/bin/activate 
# uvicorn main:app --reload
