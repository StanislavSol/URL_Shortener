from fastapi import FastAPI, Request, Body
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from shortener.validator import get_error
from shortener.normalize_url import normalize_url


app = FastAPI()
templates = Jinja2Templates(directory="shortener/templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='index.html'
    )


@app.get("/urls", response_class=HTMLResponse)
async def get_urls(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='urls/urls.html'
    )


@app.post("/urls", response_class=HTMLResponse)
async def post_urls(request: Request, url: str = Body()):
    formatted_url = normalize_url(url)
    validation_error = get_error(formatted_url)
    if validation_error:
        flash = validation_error
        return templates.TemplateResponse(
            request=request,
            name='index.html',
            context=flash
        )

