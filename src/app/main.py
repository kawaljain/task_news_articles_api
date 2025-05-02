
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from app.articles.api  import news_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"], 
    allow_headers=["*"], 
)

api_router = APIRouter(prefix="/api/v1")  # Version 1 of your API
api_router.include_router(news_router, tags=["News"])  # Include news routes under /news

@app.get('/')
def index():
    return {"message":"This is Welcome Test"}

# Include the api_router which includes news routes
app.include_router(api_router)
print("Registered Routes:", app.routes)