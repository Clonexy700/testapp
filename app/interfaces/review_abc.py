from abc import ABC, abstractmethod
from typing import List, Optional

from app.models.review import ReviewOut


class IReviewRepository(ABC):
    @abstractmethod
    def add(self, text: str, sentiment: str) -> ReviewOut:
        pass

    @abstractmethod
    def list(self, sentiment: Optional[str] = None) -> List[ReviewOut]:
        pass


class ISentimentService(ABC):
    @abstractmethod
    def analyze(self, text: str) -> str:
        pass
