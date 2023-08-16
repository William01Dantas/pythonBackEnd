from sqlalchemy import text

from app.controllers.auth.auth_handler import AuthHandler
from app.models.db.db import engine
from app.schemas.product import ProductModel


class UserService:
    def create_product(self, product: ProductModel):
        try:
            query = """
            INSERT INTO tbl_stock (name, description, data_pub, price_product, quantity)
            VALUES (:name, :description, :data_pub, :price_product, :quantity)
            """
            values = {
                "name": product.name,
                "description": product.description,
                "data_pub": product.data_pub,
                "price_product": product.price_product,
                "quantity": product.quantity
            }

            with engine.connect() as db:
                db.execute(text(query), **values)
                db.commit()

            return True, "Product created successfully"
        except Exception as e:
            return False, str(e)

    def get_all_products(self):
        query = "SELECT * FROM tbl_stock"
        with engine.connect() as db:
            result = db.execute(text(query))
            return result.fetchall()

    def get_product(self, product_id: int):
        query = "SELECT * FROM tbl_stock WHERE id_product = :product_id"
        with engine.connect() as db:
            result = db.execute(text(query), {"product_id": product_id})
            return result.fetchone()

    def remove_product(self, product_id: int):
        query = "DELETE FROM tbl_stock WHERE id_product = :product_id"
        with engine.connect() as db:
            db.execute(text(query), {"product_id": product_id})
            db.commit()

    def authenticate_user(self, username: str, password: str):
        user = self.get_user_by_username(username)
        if user and AuthHandler.verify_password(password, user.password):
            return user
