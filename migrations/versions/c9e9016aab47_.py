"""empty message

Revision ID: c9e9016aab47
Revises: efd88a3c30a8
Create Date: 2020-08-27 20:39:02.211520

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9e9016aab47'
down_revision = 'efd88a3c30a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('polar_webhook_exercises',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('polar_user_id', sa.Integer(), nullable=False),
    sa.Column('entity_id', sa.String(length=32), nullable=False),
    sa.Column('url', sa.String(length=255), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('processed', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('entity_id')
    )
    op.create_index(op.f('ix_polar_webhook_exercises_processed'), 'polar_webhook_exercises', ['processed'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_polar_webhook_exercises_processed'), table_name='polar_webhook_exercises')
    op.drop_table('polar_webhook_exercises')
    # ### end Alembic commands ###
