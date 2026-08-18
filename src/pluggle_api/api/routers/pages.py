from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from pluggle_api.settings import STATIC_DIR, TEMPLATES_DIR
from pluggle.interfaces.api.api import list_available_strategies

router = APIRouter()

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


@router.get("/")
def root():
    return RedirectResponse(url="/home")


@router.get("/home", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="home.html", context={"strategies": list_available_strategies()}
    )


@router.get("/how-it-works", response_class=HTMLResponse)
def how_it_works(request: Request):
    return templates.TemplateResponse(request, "how_it_works.html", {})


@router.get("/strategies", response_class=HTMLResponse)
def strategies(request: Request):
    return templates.TemplateResponse(request, "strategies.html", {})


@router.get("/about", response_class=HTMLResponse)
def about(request: Request):
    return templates.TemplateResponse(request, "about.html", {})
