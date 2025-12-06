from fastapi import HTTPException, status
from typing import List
from uuid import UUID, uuid4

from app.products.dtos import CreateProductDto, UpdateProductDto
from app.products.entity import Product
from app.products.repository import ProductsRepository


class ProductsService:
    def __init__(self, repository: ProductsRepository):
        self.__repository = repository

    def create(self, create_dto: CreateProductDto) -> Product:
        new_product = Product(
            id=uuid4(),
            name=create_dto.name,
            price=create_dto.price,
        )
        return self.__repository.add(new_product)

    def find_all(self) -> List[Product]:
        return self.__repository.list_all()

    def find_one(self, product_id: UUID) -> Product:
        product = self.__repository.get_by_id(product_id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with id {product_id} not found",
            )
        return product

    def update(self, product_id: UUID, update_dto: UpdateProductDto) -> Product:
        product = self.find_one(product_id)

        if update_dto.name is not None:
            product.name = update_dto.name
        if update_dto.price is not None:
            product.price = update_dto.price

        return self.__repository.update(product)

    def remove(self, product_id: UUID) -> Product:
        product = self.find_one(product_id)
        self.__repository.remove(product_id)
        return product
