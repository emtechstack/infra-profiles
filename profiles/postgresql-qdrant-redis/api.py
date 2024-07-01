from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers.router_hello_world import router as hello_world_router
from routers.router_home import router as home_router

from utils.router_manager import RouterManager

app = FastAPI(
    title='EmTeckStack API',
    version='0.1.0',
)

# Add static files directory
app.mount("/statics", StaticFiles(directory="statics"), name="statics")

# Automatically load and include routers
RouterManager.load_and_include_routers(app)