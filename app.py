from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from api_v1 import router as router_v1
from core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router_v1, prefix=settings.api_v1_prefix)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
