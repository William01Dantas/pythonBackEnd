from fastapi import FastAPI

from app.controllers.routers.user_router import user_router
from app.controllers.routers.product_router import product_router

app = FastAPI()

app.include_router(user_router)
app.include_router(product_router)