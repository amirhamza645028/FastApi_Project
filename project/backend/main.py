from fastapi import FastAPI
from core.config import settings
from  apis.base  import base_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
)
app.include_router.router(base_router)

@app.get("/")
def hello_api():
    return {"msg":"Hello FastAPI"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port= 8000, reload=True)