from fastapi import APIRouter, Depends
from app.controllers.auth.auth_handler import AuthHandler

protect_router = APIRouter()

@protect_router.get("/protected-route")
async def protected_route(current_user: str = Depends(AuthHandler.get_current_user)):
    return {"message": f"This is a protected route for user: {current_user}"}
