# src/schemas/request.py
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field

class GeminiModels(str, Enum):
    FLASH_1_5 = "gemini-1.5-flash"
    FLASH_2_0 = "gemini-2.0-flash"
    FLASH_THINKING = "gemini-2.0-flash-thinking"
    FLASH_THINKING_WITH_APPS = "gemini-2.0-flash-thinking-with-apps"
    FLASH_2_5 = "gemini-2.5-flash"
    PRO_2_5 = "gemini-2.5-pro"
    EXP_ADVANCED_2_5 = "gemini-2.5-exp-advanced"

class GeminiRequest(BaseModel):
    message: str
    model: GeminiModels = Field(default=GeminiModels.FLASH_2_0, description="Model to use for Gemini.")
    images: Optional[List[str]] = []

class OpenAIChatRequest(BaseModel):
    messages: List[dict]
    model: Optional[GeminiModels] = None
    stream: Optional[bool] = False
