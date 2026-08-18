from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from pluggle_api.settings import STATIC_DIR
from pluggle_api.api.routers.pages import router as pages_router

app = FastAPI()
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

app.include_router(pages_router, tags=["pages"])
