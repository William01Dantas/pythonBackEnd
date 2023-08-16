from pydantic import BaseModel

class ProductModel(BaseModel):
    name: str
    description: str
    data_pub: str
    price_product: float
    quantity: float
