import torch
from transformers import pipeline
from app.config import get_settings


class SentimentService:
    """
    Используем ru bert для распознования.
    """

    def __init__(self):
        cfg = get_settings()
        self.analyzer = pipeline(
            task="text-classification",
            model=cfg.HF_MODEL,
            tokenizer=cfg.HF_MODEL
        )

    def analyze(self, text: str) -> str:
        result = self.analyzer(text[:8192])
        label = result[0]["label"].upper()
        if label in ("POS", "POSITIVE"):
            return "positive"
        if label in ("NEG", "NEGATIVE"):
            return "negative"
        return "neutral"
