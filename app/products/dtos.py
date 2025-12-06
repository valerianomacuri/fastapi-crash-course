from pydantic import BaseModel, Field
from typing import Optional


class CreateProductDto(BaseModel):
    name: str
    price: float = Field(default=None, ge=0)


class UpdateProductDto(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = Field(default=None, ge=0)
