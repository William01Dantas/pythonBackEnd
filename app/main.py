from fastapi import FastAPI

from app.controllers.routers.product_router import product_router
from app.controllers.routers.user_router import user_router

app = FastAPI()

app.include_router(user_router)
app.include_router(product_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="172.17.192.1", port=8000)
