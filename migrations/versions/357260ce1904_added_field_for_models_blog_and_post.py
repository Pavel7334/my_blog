"""added field for models Blog and Post

Revision ID: 357260ce1904
Revises: 67ebcf7e63f7
Create Date: 2023-09-08 16:32:52.595336

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '357260ce1904'
down_revision: Union[str, None] = '67ebcf7e63f7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
