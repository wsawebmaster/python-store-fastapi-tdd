from decimal import Decimal
from typing import Annotated, Optional
from bson import Decimal128
from datetime import datetime
from uuid import UUID, uuid4
from pydantic import AfterValidator, Field, BaseModel
from store.schemas.base import BaseSchemaMixin


class ProductBase(BaseModel):
    name: str = Field(..., description="Product name")
    quantity: int = Field(..., description="Product quantity")
    price: float = Field(..., description="Product price")
    status: bool = Field(..., description="Product status")


class ProductIn(ProductBase, BaseSchemaMixin):
    ...


class ProductOut(ProductIn):
    id: UUID = Field(default_factory=uuid4, description="Identificador do produto")
    created_at: datetime = Field(
        default_factory=datetime.utcnow, description="Data de criação"
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow, description="Data de atualização"
    )


def convert_decimal_128(v):
    return Decimal128(str(v))


Decimal_ = Annotated[Decimal, AfterValidator(convert_decimal_128)]


class ProductUpdate(BaseSchemaMixin):
    quantity: Optional[int] = Field(None, description="Product quantity")
    price: Optional[Decimal_] = Field(None, description="Product price")
    status: Optional[bool] = Field(None, description="Product status")


class ProductUpdateOut(ProductOut):
    ...
