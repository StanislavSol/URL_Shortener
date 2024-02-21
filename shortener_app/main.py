from fastapi import FastAPI, Request, Body, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from shortener_app.handlers_url import normalize_url, get_error
from shortener_app.crud import add_url_info, get_url, get_db
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os


load_dotenv()
BASE_URL = os.getenv('BASE_URL')


app = FastAPI()
templates = Jinja2Templates(directory="shortener_app/templates")


@app.get("/")
async def index(request: Request):
    '''Home page'''
    return templates.TemplateResponse(
        request=request,
        name='index.html'
    )


@app.post("/")
async def post_urls(
        request: Request,
        data: str = Body(),
        db: Session = Depends(get_db)):
    '''Shortening the link'''

    target_url, key = await normalize_url(data, db)
    validation_error = await get_error(target_url, key, db)

    if validation_error:
        context = validation_error
        return templates.TemplateResponse(
            request=request,
            name='index.html',
            context=context
        )

    url_key = await add_url_info(target_url, key, db)
    short_url = f'{BASE_URL}/{url_key}'

    context = {
        'message': f'Страница успешно сокращена: {short_url}',
        'category': 'success',
    }
    return templates.TemplateResponse(
        request=request,
        name='index.html',
        context=context
    )


@app.get("/{url_key}")
async def forward_to_target_url(
        url_key: str,
        request: Request,
        db: Session = Depends(get_db)):
    '''Follow shortened link'''

    db_url = await get_url(url_key, db)

    if db_url:
        return RedirectResponse(db_url.target_url)

    context = {
        'message': 'Такого URL не существует.',
        'category': 'danger',
    }

    return templates.TemplateResponse(
        request=request,
        name='index.html',
        context=context
    )
