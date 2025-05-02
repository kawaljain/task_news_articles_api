from fastapi import FastAPI 
from pydantic import BaseModel 

app = FastAPI()

@app.get('/')
def index():
    return {"message":"This is Welcome Test"}

@app.get('/search/{user}')
async def search(user:str):
    return {"message":f"This is Welcome {user}"}
    