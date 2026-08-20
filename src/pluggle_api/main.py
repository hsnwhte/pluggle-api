from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from pluggle_api.api.routers.routes import router as pages_router
from pluggle_api.settings import STATIC_DIR

app = FastAPI()
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

app.include_router(pages_router, tags=["pages"])
