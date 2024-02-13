from fastapi import FastAPI, Request, Body
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel


app = FastAPI()
templates = Jinja2Templates(directory="shortener/templates")

class Item(BaseModel):
        url: str

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name='index.html')


@app.get("/urls", response_class=HTMLResponse)
async def get_urls(request: Request):
    return templates.TemplateResponse(request=request, name='urls/urls.html')


@app.post("/urls", response_class=HTMLResponse)
async def post_urls(request: Request, item: Item):
    url = item
    print(url)
    return RedirectResponse(request.url_for("index"))
