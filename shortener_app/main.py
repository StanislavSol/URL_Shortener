from fastapi import FastAPI, Request, Body, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from shortener_app.handlers_url import (
                                        get_short_url,
                                        normalize_url,
                                        get_error,
                                        )
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models
import secrets

app = FastAPI()
templates = Jinja2Templates(directory="shortener_app/templates")
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='index.html'
    )


@app.post("/", response_class=HTMLResponse)
async def post_urls(request: Request, data: str = Body(), db: Session = Depends(get_db)):
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


    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = "".join(secrets.choice(chars) for _ in range(5))

    db_url = models.URL(
        target_url=formatted_url, key=key
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    db_url.url = key
    print(db_url.url)

    flash = {
        'message': f'Страница успешно сокращена: {short_url}',
        'category': 'success'
    }
    return templates.TemplateResponse(
        request=request,
        name='index.html',
        context=flash
    )

@app.get("/{url_key}")
def forward_to_target_url(
        url_key: str,
        request: Request,
        db: Session = Depends(get_db)
    ):
    db_url = (
        db.query(models.URL)
        .filter(models.URL.key == url_key)
        .first()
    )
    if db_url:
        return RedirectResponse(db_url.target_url)
