from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional

from app.schemas.review import ReviewIn, ReviewOut
from app.interfaces.review_abc import IReviewService
from app.dependencies import get_review_service

router = APIRouter(prefix="/reviews", tags=["reviews"])


@router.post("/", response_model=ReviewOut)
def create_review(
        payload: ReviewIn,
        service: IReviewService = Depends(get_review_service)
) -> ReviewOut:
    text = payload.text.strip()
    if not text:
        raise HTTPException(400, "Review text cannot be empty")
    return service.create_review(text)


@router.get("/", response_model=List[ReviewOut])
def list_reviews(
        sentiment: Optional[str] = Query(None, enum=["positive", "negative", "neutral"]),
        service: IReviewService = Depends(get_review_service)
) -> List[ReviewOut]:
    return service.list_reviews(sentiment)
