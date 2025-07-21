from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional

from app.models import ReviewIn, ReviewOut
from app.interfaces import IReviewRepository, ISentimentService
from app.repository import ReviewRepository
from app.services.sentiment_service import SentimentService


router = APIRouter(prefix="/reviews", tags=["reviews"])
repo = ReviewRepository()
service = SentimentService()


@router.post("/", response_model=ReviewOut)
def create_review(
        payload: ReviewIn,
        repo: IReviewRepository = Depends(get_repository),
        service: ISentimentService = Depends(get_sentiment_service)
):
    text = payload.text.strip()
    if not text:
        raise HTTPException(400, "Review text cannot be empty")
    sentiment = service.analyze(text)
    return repo.add(text, sentiment)


@router.get("/", response_model=List[ReviewOut])
def list_reviews(
        sentiment: Optional[str] = Query(None, enum=["positive", "negative", "neutral"]),
        repo: IReviewRepository = Depends(get_repository)
):
    return repo.list(sentiment)
