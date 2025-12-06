from fastapi import FastAPI

from app.products.routes import router as product_router

app = FastAPI()

app.include_router(product_router)


@app.get("/")
def root():
    return {"message": "API is running"}
