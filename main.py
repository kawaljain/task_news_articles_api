from fastapi import FastAPI,HTTPException,APIRouter
from config.app import AppSettings
import httpx
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

appSettings = AppSettings()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"], 
    allow_headers=["*"], 
)

api_router = APIRouter(prefix="/api/v1")

@app.get('/')
def index():
    return {"message":"This is Welcome Test"}

@api_router.get('/')
def index():
    return {"message":"This is Welcome Test"}

@api_router.get('/news/search')
async def search(name: Optional[str] = None):

    if not name:
        raise HTTPException(status_code=400, detail="Name is required")

    url = appSettings.SERPER_API_URL
    headers = {
        "X-API-KEY": appSettings.SERPER_API_KEY,
        "Content-Type": "application/json", 
    }
    payload ={
        "q": name
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=headers,json=payload)
            response.raise_for_status()  
            data = response.json()
            return {"articles": data.get("news", [])} 
        except httpx.HTTPStatusError as e:
            # Log and other action done here. use for debug And Store logs in db
            print(e.response)
            raise HTTPException(status_code=e.response.status_code, detail=f"API Error: Something Went Wrong Try after some time")
        except Exception as e:
            # Log and other action done here. use for debug And Store logs in db
            print(e)
            raise HTTPException(status_code=500, detail="API Error: Something Went Wrong Try after some time")
    return {"message":f"This is Welcome {user}"}
    
app.include_router(api_router)