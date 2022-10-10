"""upgade Tank models

Revision ID: 5ce7815d2195
Revises: 6b7d7e96ddad
Create Date: 2022-10-06 20:05:40.386558

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ce7815d2195'
down_revision = '6b7d7e96ddad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tank', sa.Column('yeasts_id', sa.Integer(), nullable=True))
    op.add_column('tank', sa.Column('expected_volume', sa.Integer(), nullable=False))
    op.create_index(op.f('ix_tank_yeasts_id'), 'tank', ['yeasts_id'], unique=False)
    op.create_foreign_key(None, 'tank', 'yeasts', ['yeasts_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tank', type_='foreignkey')
    op.drop_index(op.f('ix_tank_yeasts_id'), table_name='tank')
    op.drop_column('tank', 'expected_volume')
    op.drop_column('tank', 'yeasts_id')
    # ### end Alembic commands ###
