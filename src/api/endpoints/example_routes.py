from fastapi import APIRouter

example_routes = APIRouter()

@example_routes.get('/health')
def health():
    return 'Service healthy!'

@example_routes.get('/test_endpoint')
def test_endpoint():
    return 'This is a test endpoint'