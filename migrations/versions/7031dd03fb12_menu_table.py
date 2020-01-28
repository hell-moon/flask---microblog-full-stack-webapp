"""menu table

Revision ID: 7031dd03fb12
Revises: d64a2fb2b0c1
Create Date: 2020-01-21 21:35:12.048868

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7031dd03fb12'
down_revision = 'd64a2fb2b0c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('menu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('description', sa.String(length=1024), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('menu')
    # ### end Alembic commands ###
