from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from core.models.product import Product

from . import crud
from .dependencies import product_by_id
from .schemas import ProductCreateSchema, ProductSchema, ProductUpdateSchema

router = APIRouter(
    tags=["Products"],
)


@router.get(
    "/",
    response_model=list[ProductSchema],
    status_code=status.HTTP_200_OK,
)
async def get_products(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> list[Product]:
    return await crud.get_products(session=session)


@router.post(
    "/",
    response_model=ProductSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_product(
    product_in: ProductCreateSchema,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Product:
    return await crud.create_product(session=session, product_in=product_in)


@router.get(
    "/{product_id}/",
    response_model=ProductSchema,
    status_code=status.HTTP_200_OK,
)
async def get_product(
    product: Product = Depends(product_by_id),
) -> Product:
    return product


@router.patch(
    "/{product_id}/",
    response_model=ProductSchema,
    status_code=status.HTTP_200_OK,
)
async def update_product(
    product_update: ProductUpdateSchema,
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Product:
    return await crud.update_product(
        session=session,
        product=product,
        product_update=product_update,
    )


@router.delete(
    "/{product_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_product(
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_product(session=session, product=product)
