from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .api import auth, businesses, packages


app = FastAPI(title='Salvio API')


@app.get('/health')
def health():
    return {
        "status": "healthy",
        "service": "salvio-api"
    }


app.include_router(auth.router, prefix='/auth', tags=['auth'])
app.include_router(businesses.router, prefix='/businesses', tags=['businesses'])
app.include_router(packages.router, prefix='/packages', tags=['packages'])
