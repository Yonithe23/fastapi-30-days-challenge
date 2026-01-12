from fastapi import FastAPI , Query
from typing import Annotated

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[ str | None , Query(max_length=50)] = None):
    #async def read_items(q: str | None = Query(default=None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results