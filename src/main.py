import uvicorn

from src.core.config import initialize_app

app = initialize_app()

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)