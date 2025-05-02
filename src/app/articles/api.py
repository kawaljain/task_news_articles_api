from fastapi import APIRouter
from typing import Optional
from .service import getArticlesByName

news_router = APIRouter(prefix="/news")

@news_router.get('/')
def index():
    return {"message":"This is Welcome Test"}

@news_router.get('/search')
async def search(name: Optional[str] = None):
    return await getArticlesByName(name)
    