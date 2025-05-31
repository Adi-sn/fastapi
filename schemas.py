from pydantic import BaseModel
from typing import List

class Textpart(BaseModel):
    text: str

class next(BaseModel):
    parts: List[Textpart]

class content(BaseModel):
    contents: List[next]
    