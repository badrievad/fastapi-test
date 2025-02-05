from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.product import Product

from ..products.schemas import ProductCreateSchema, ProductUpdateSchema


async def get_products(session: AsyncSession) -> list[Product]:
    stmt = select(Product).order_by(Product.id)
    result: Result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)


async def get_product(session: AsyncSession, product_id: int) -> Product | None:
    return await session.get(Product, product_id)


async def create_product(
    session: AsyncSession, product_in: ProductCreateSchema
) -> Product:
    product = Product(**product_in.model_dump())
    session.add(product)
    try:
        await session.commit()
    except Exception:
        await session.rollback()
        raise
    await session.refresh(product)
    return product


async def update_product(
    session: AsyncSession,
    product: Product,
    product_update: ProductUpdateSchema,
) -> Product:

    update_data = product_update.model_dump(exclude_unset=True)

    if not update_data:
        # Если нет изменений, возвращаем продукт без изменений
        return product

    # Обновляем только те поля, которые явно заданы в запросе
    for key, value in update_data.items():
        setattr(product, key, value)

    try:
        await session.commit()
    except Exception:
        await session.rollback()
        raise

    await session.refresh(product)
    return product


async def delete_product(session: AsyncSession, product: Product) -> None:
    await session.delete(product)
    await session.commit()
