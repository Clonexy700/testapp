import torch
from transformers import pipeline
from typing import Optional, List

from app.interfaces.review_abc import IReviewService
from app.repositories.review_repo import ReviewRepository
from app.schemas.review import ReviewOut
from app.config import get_settings


class ReviewService(IReviewService):
    def __init__(self):
        self.repo = ReviewRepository()
        cfg = get_settings()
        self.analyzer = pipeline(
            task="text-classification",
            model=cfg.HF_MODEL,
            tokenizer=cfg.HF_MODEL
        )

    def create_review(self, text: str) -> ReviewOut:
        sentiment = self._analyze(text)
        return self.repo.add(text, sentiment)

    def list_reviews(self, sentiment: Optional[str] = None) -> List[ReviewOut]:
        return self.repo.list(sentiment)

    def _analyze(self, text: str) -> str:
        result = self.analyzer(text[:8192])
        lab = result[0]["label"].upper()
        if lab in ("POS", "POSITIVE"):
            return "positive"
        if lab in ("NEG", "NEGATIVE"):
            return "negative"
        return "neutral"
