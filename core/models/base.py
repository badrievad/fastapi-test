from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column

from ..utils import camel_to_snake


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        # Преобразуем имя класса в snake_case и добавляем 's' для образования множественного числа
        return camel_to_snake(cls.__name__) + "s"

    id: Mapped[int] = mapped_column(primary_key=True)
