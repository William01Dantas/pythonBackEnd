from app.controllers.auth.auth_handler import AuthHandler
from app.models.user.user import User


class UserService:
    def __init__(self):
        # Cria um usuário fictício para testes
        self.users = {
            "testuser@test.com": User(username="testuser@test.com", password=AuthHandler.get_password_hash("12345678"))
        }

    def authenticate_user(self, username: str, password: str):
        user = self.get_user_by_username(username)
        if user:
            if AuthHandler.verify_password(password, user.password):
                print("Authentication successful")
                return user
            else:
                print("Password mismatch")
        else:
            print("User not found")

    def get_user_by_username(self, username):
        return self.users.get(username)
