"""added a field for the model Comment

Revision ID: 67ebcf7e63f7
Revises: e39421257999
Create Date: 2023-09-05 13:28:10.839745

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '67ebcf7e63f7'
down_revision: Union[str, None] = 'e39421257999'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('posts_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'posts', ['posts_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'posts_id')
    # ### end Alembic commands ###
