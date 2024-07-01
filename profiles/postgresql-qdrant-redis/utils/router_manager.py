from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
import glob
import importlib.util
import os

class RouterManager:
    def __init__(self):
        pass

    @staticmethod
    def load_and_include_routers(app):
        router_files = glob.glob("routers/**/*.py", recursive=True)
        for router_file in router_files:
            module_name = router_file.replace("/", ".").replace("\\", ".").rstrip(".py")
            spec = importlib.util.spec_from_file_location(module_name, router_file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "router") and isinstance(module.router, APIRouter):
                app.include_router(module.router)
            else:
                print(
                    f"Could not add {module_name} because it's not an APIRouter instance."
                )