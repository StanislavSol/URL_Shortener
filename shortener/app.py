from fastapi import FastAPI, Request, Body
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from shortener.validator import get_error
from shortener.normalize_url import get_short_url, normalize_url
from shortener import db
from dotenv import load_dotenv
import os


load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
app = FastAPI()
templates = Jinja2Templates(directory="shortener/templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='index.html'
    )


@app.post("/", response_class=HTMLResponse)
async def post_urls(request: Request, data: str = Body()):
    formatted_url = normalize_url(data)
    validation_error = get_error(formatted_url)
    if validation_error:
        flash = validation_error
        return templates.TemplateResponse(
            request=request,
            name='index.html',
            context=flash
        )
    short_url = get_short_url(formatted_url)
    flash = {
        'message': f'Страница успешно сокращена: {short_url}',
        'category': 'success'
    }
    return templates.TemplateResponse(
        request=request,
        name='index.html',
        context=flash
    )
