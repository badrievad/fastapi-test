"""add count to order product association table

Revision ID: 4d912276051a
Revises: 8c5cb8b22544
Create Date: 2025-02-08 17:23:54.350550

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4d912276051a"
down_revision: Union[str, None] = "8c5cb8b22544"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "order_product_associations",
        sa.Column("count", sa.Integer(), server_default="1", nullable=False),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("order_product_associations", "count")
    # ### end Alembic commands ###
