from pydantic import BaseModel, ConfigDict


class ProductBaseSchema(BaseModel):

    name: str
    price: float
    description: str


class ProductSchema(ProductBaseSchema):
    model_config = ConfigDict(from_attributes=True)

    id: int


class ProductCreateSchema(ProductBaseSchema):
    pass

class ProductUpdateSchema(BaseModel):
    name: str | None = None
    price: float | None = None
    description: str | None = None
    