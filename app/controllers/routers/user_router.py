from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
import logging
from app.controllers.services.user_service import UserService
from app.controllers.auth.auth_handler import AuthHandler

user_router = APIRouter()


@user_router.post("/token")
async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends()
):
    user_service = UserService()

    logging.basicConfig(level=logging.DEBUG)

    logging.debug(f"Login attempt: username={form_data.username}, password={form_data.password}")

    user = user_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        logging.debug("Authentication failed")

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=AuthHandler.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = AuthHandler.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    logging.debug("Authentication successful")

    return {"access_token": access_token, "token_type": "bearer"}
