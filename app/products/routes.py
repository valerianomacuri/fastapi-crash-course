from uuid import UUID
from fastapi import APIRouter
from typing import List

from app.products.dtos import CreateProductDto, UpdateProductDto
from app.products.entity import Product
from app.products.repository import ProductsRepository
from app.products.service import ProductsService

products_repository = ProductsRepository()
products_service = ProductsService(products_repository)

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=Product)
def create_product(dto: CreateProductDto):
    return products_service.create(dto)


@router.get("/", response_model=List[Product])
def get_products():
    return products_service.find_all()


@router.get("/{product_id}", response_model=Product)
def get_product(product_id: UUID):
    return products_service.find_one(product_id)


@router.put("/{product_id}", response_model=Product)
def update_product(product_id: UUID, dto: UpdateProductDto):
    return products_service.update(product_id, dto)


@router.delete("/{product_id}", response_model=Product)
def delete_product(product_id: UUID):
    return products_service.remove(product_id)
