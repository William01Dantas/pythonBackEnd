from fastapi import APIRouter, HTTPException

from app.controllers.services.user_service import UserService
from app.schemas.product import ProductModel

product_router = APIRouter()

@product_router.post("/products", status_code=201)
def add_product(product: ProductModel):
    product_service = UserService()
    success, result = product_service.create_product(product)
    if success:
        return result
    else:
        raise HTTPException(status_code=400, detail=result)

@product_router.get("/products")
def list_products():
    product_service = UserService()
    return product_service.get_all_products()

@product_router.get("/products/{product_id}")
def get_product_details(product_id: int):
    product_service = UserService()
    product = product_service.get_product(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@product_router.delete("/products/{product_id}", status_code=204)
def delete_product(product_id: int):
    product_service = UserService()
    product_service.remove_product(product_id)
    return None
