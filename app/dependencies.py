from fastapi import Depends

from app.interfaces.review_abc import IReviewRepository, ISentimentService
from app.repositories.review_repo import ReviewRepository
from app.services.sentiment_service import SentimentService


def get_repository() -> IReviewRepository:
    return ReviewRepository()


def get_sentiment_service() -> ISentimentService:
    return SentimentService()
