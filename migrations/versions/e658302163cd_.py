"""empty message

Revision ID: e658302163cd
Revises: d7302317db0d
Create Date: 2019-11-29 17:03:14.429141

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e658302163cd'
down_revision = 'd7302317db0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('weight', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'weight')
    # ### end Alembic commands ###
