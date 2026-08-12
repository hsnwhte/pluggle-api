from email import message_from_binary_file

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pluggle_api.settings import STATIC_DIR, TEMPLATES_DIR

app = FastAPI()
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=TEMPLATES_DIR)

AVAILABLE_STRATEGIES = ["default", "8d_excel_mapper_v1"]


@app.get("/")
def get_home(request: Request):
    return templates.TemplateResponse(
        request=request, name="home.html", context={"strategies": AVAILABLE_STRATEGIES}
    )


@app.get("/strategies")
def get_strategies():
    return {"message": "Strategies"}


@app.get("/how-it-works")
def get_how_it_works():
    return {"message": "How It Works"}


@app.get("/about")
def get_about():
    return {"message": "About"}
