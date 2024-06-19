from fastapi import APIRouter, File, UploadFile, Form, HTTPException, Request

from fastapi.responses import StreamingResponse, JSONResponse

from pathlib import Path
import shutil
import asyncio
from dotenv import load_dotenv

from sse_starlette.sse import EventSourceResponse

load_dotenv()

router = APIRouter(prefix="/say", tags=["Router 1"])

@router.get("/", response_class=JSONResponse)
async def hello(request: Request):
    return {"answer": "hello"}
