from fastapi import APIRouter, Form, Request, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pluggle.enums import ContentFormat
from pluggle.exceptions.errors import StrategyNotFoundError
from pluggle.interfaces.api.api import list_available_strategies, run

from pluggle_api.adapters import build_input_args
from pluggle_api.schemas.input import InputFormData
from pluggle_api.settings import OUTPUTS_DIR, TEMPLATES_DIR

router = APIRouter()

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


@router.get("/")
def root():
    return RedirectResponse(url="/home")


@router.get("/home", response_class=HTMLResponse)
def home(request: Request):
    try:
        available_strategies = list_available_strategies()
    except StrategyNotFoundError:
        available_strategies = []
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={
            "strategies": available_strategies,
            "target_formats": [f.value for f in ContentFormat],
        },
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


@router.post("/run")
def run_pipeline(
    strategy: str = Form(...),
    source_url: str | None = Form(None),
    source_file: UploadFile | None = None,
    target_format: ContentFormat = Form(...),
):
    form_data = InputFormData(
        strategy=strategy,
        source_url=source_url,
        source_filepath=source_file.path,
        target_format=target_format,
    )
    args = build_input_args(form_data)

    report = run(args=args)
    return {
        "status": "success",
        "report": report,
        "download_url": str(OUTPUTS_DIR / {...}),
    }
