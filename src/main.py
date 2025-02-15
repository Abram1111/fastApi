import uvicorn
from fastapi import FastAPI
from config import settings
from route import router

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        reload=settings.DEBUG_MODE, 
        host=settings.DOMAIN, 
        port=settings.BACKEND_PORT
        )
    
