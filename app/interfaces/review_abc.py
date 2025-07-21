from abc import ABC, abstractmethod
from typing import List, Optional

from app.schemas.review import ReviewOut


class IReviewRepository(ABC):
    @abstractmethod
    def add(self, text: str, sentiment: str) -> ReviewOut:
        pass

    @abstractmethod
    def list(self, sentiment: Optional[str] = None) -> List[ReviewOut]:
        pass


class IReviewService(ABC):
    @abstractmethod
    def create_review(self, text: str) -> ReviewOut:
        pass

    @abstractmethod
    def list_reviews(self, sentiment: Optional[str] = None) -> List[ReviewOut]:
        pass

    @abstractmethod
    def _analyze(self, text: str) -> str:
        pass
