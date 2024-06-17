from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(tags=["Home"])


@router.get("/", response_class=HTMLResponse)
async def welcome(request: Request):
    html_content = Path("statics/pages/landing_page.html").read_text()
    return HTMLResponse(content=html_content)
