import jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from app.settings.setting import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

class AuthHandler:
    SECRET_KEY = settings.SECRET_KEY
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    @staticmethod
    def create_access_token(data: dict, expires_delta: timedelta):
        to_encode = data.copy()
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, AuthHandler.SECRET_KEY, algorithm=AuthHandler.ALGORITHM)
        return encoded_jwt

    async def get_current_user(token: str = Depends(oauth2_scheme)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, AuthHandler.SECRET_KEY, algorithms=[AuthHandler.ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
        except jwt.ExpiredSignatureError:
            raise credentials_exception
        except jwt.JWTError:
            raise credentials_exception

        return username

    @classmethod
    def verify_password(cls, plain_password, hashed_password):
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return pwd_context.verify(plain_password, hashed_password)

    @classmethod
    def get_password_hash(cls, password: str):
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return pwd_context.hash(password)
