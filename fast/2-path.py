from fastapi import FastAPI

app = FastAPI()

@app.get("/item/{value}") 

async def read_item(value :int):
    return{"item":value}