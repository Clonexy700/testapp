from fastapi import Depends

from app.interfaces.review_abc import IReviewService
from app.services.review_service import ReviewService


def get_review_service() -> IReviewService:
    return ReviewService()
