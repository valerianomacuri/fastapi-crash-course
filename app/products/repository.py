from typing import List, Optional
from uuid import UUID, uuid4

from app.products.entity import Product

fake_products: List[Product] = [
    Product(id=str(uuid4()), name="Keyboard", price=50),
    Product(id=str(uuid4()), name="Mouse", price=20),
]


class ProductsRepository:
    def __init__(self):
        self.__products: List[Product] = fake_products

    def create(self, product: Product) -> Product:
        self.__products.append(product)
        return product

    def find_all(self) -> List[Product]:
        return self.__products

    def find_by_id(self, product_id: UUID) -> Optional[Product]:
        for product in self.__products:
            if product.id == product_id:
                return product
        return None

    def update(self, product: Product) -> Product:
        for i, p in enumerate(self.__products):
            if p.id == product.id:
                self.__products[i] = product
                return product
        return product

    def remove(self, product_id: str) -> Optional[Product]:
        product = self.find_by_id(product_id)
        if product:
            self.__products = [p for p in self.__products if p.id != product_id]
        return product
