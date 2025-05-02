from typing import Optional
import httpx
from fastapi import HTTPException
from app.core.appSettings import appSettings  # or wherever you store config


async def getArticlesByName(name: Optional[str] = None):

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
    
    return HTTPException(status_code=500, detail="API Error: Something Went Wrong Try after some time")
    