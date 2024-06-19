from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers.router_hello_world import router as hello_world_router
from routers.router_home import router as home_router

app = FastAPI()
app.mount("/statics", StaticFiles(directory="statics"), name="statics")

# Include the router
app.include_router(hello_world_router)
app.include_router(home_router)
