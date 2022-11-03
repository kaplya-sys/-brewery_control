"""empty message

Revision ID: 29b74c05be79
Revises: 1099e5a4a65f
Create Date: 2022-10-28 15:13:32.555152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29b74c05be79'
down_revision = '1099e5a4a65f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stock',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_product', sa.String(length=100), nullable=False),
    sa.Column('type_product', sa.Enum('malt', 'hop', 'yeast', 'other', name='producttype'), nullable=False),
    sa.Column('amount_product', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name_product')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stock')
    # ### end Alembic commands ###
