from fastapi import FastAPI, Depends

from src.api.endpoints import example_routes
from src.api.middleware import check_api_key

def configure_app(app: FastAPI):
    pass

def initialize_app():
    app = FastAPI()

    configure_app(app)

    app.include_router(example_routes, dependencies=[Depends(check_api_key)])

    return app