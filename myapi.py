# fast API
# RESTful API (GET, POST)
from fastapi import FastAPI

app = FastAPI()

@app.get("/encore/") # 데코레이터
async def myfunc(): # 비동기 async
    return {"message" : "ㅋㅋㅋ"}

