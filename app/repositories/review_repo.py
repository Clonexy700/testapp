import sqlite3
from typing import Optional, List
from datetime import datetime, timezone

from app.schemas.review import ReviewOut
from app.interfaces.review_abc import IReviewRepository
from app.config import get_settings


class ReviewRepository(IReviewRepository):
    def __init__(self):
        cfg = get_settings()
        relative = cfg.DATABASE_URL.replace("sqlite:///", "")
        self.db_file = str(relative)
        self._init_db()

    def _get_conn(self):
        conn = sqlite3.connect(self.db_file, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self):
        ddl = '''
        CREATE TABLE IF NOT EXISTS reviews (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          text TEXT NOT NULL,
          sentiment TEXT NOT NULL,
          created_at TEXT NOT NULL
        );
        '''
        conn = self._get_conn(); conn.execute(ddl); conn.commit(); conn.close()

    def add(self, text: str, sentiment: str) -> ReviewOut:
        created_at = datetime.now(timezone.utc).isoformat()
        conn = self._get_conn(); cur = conn.cursor()
        cur.execute(
            "INSERT INTO reviews (text, sentiment, created_at) VALUES (?, ?, ?)",
            (text, sentiment, created_at)
        )
        conn.commit(); rid = cur.lastrowid; conn.close()
        return ReviewOut(id=rid, text=text, sentiment=sentiment, created_at=created_at)

    def list(self, sentiment: Optional[str] = None) -> List[ReviewOut]:
        conn = self._get_conn(); cur = conn.cursor()
        if sentiment:
            cur.execute("SELECT * FROM reviews WHERE sentiment = ? ORDER BY id", (sentiment,))
        else:
            cur.execute("SELECT * FROM reviews ORDER BY id")
        rows = cur.fetchall(); conn.close()
        return [ReviewOut(**dict(row)) for row in rows]
