import uvicorn
from fastapi import FastAPI
from users.views import router as user_router
from contextlib import asynccontextmanager
from core.models import db_helper, Base
from core.config import settings
from api_v1 import router as router_v1


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(user_router)
app.include_router(router_v1, prefix=settings.api_v1_prefix)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
