from fastapi import FastAPI

from src.api.endpoints import example_routes

def configure_app(app: FastAPI):
    pass

def initialize_app():
    app = FastAPI()

    configure_app(app)

    app.include_router(example_routes)
    return app