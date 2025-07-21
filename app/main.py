from fastapi import FastAPI
from app.routers.reviews import router as reviews_router


app = FastAPI(title="Review Sentiment Service")
app.include_router(reviews_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
