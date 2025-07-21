from pydantic import BaseModel
from datetime import datetime


class ReviewIn(BaseModel):
    text: str


class ReviewOut(BaseModel):
    id: int
    text: str
    sentiment: str
    created_at: datetime
