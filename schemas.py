from pydantic import BaseModel
from typing import List

class TranslationRequest(BaseModel):
    banglish: str

class TranslationResponse(BaseModel):
    id: int 
    banglish: str
    bangla: str
    