from fastapi import APIRouter

example_routes = APIRouter()

@example_routes.get('/health')
def health():
    return 'Service healthy!'