"""Initial Demo Table.

Revision ID: 313cfc71a065
Revises: a639228ac6a2
Create Date: 2020-12-17 13:51:36.260457

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '313cfc71a065'
down_revision = 'a639228ac6a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('demo_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('added_time', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('update_time', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('name', sa.String(length=256), server_default='', nullable=False),
    sa.Column('age', sa.Integer(), server_default=sa.text('-1'), nullable=False),
    sa.Column('sex', sa.SMALLINT(), server_default=sa.text('-1'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('demo_model')
    # ### end Alembic commands ###