"""empty message

Revision ID: e808748ac145
Revises: 
Create Date: 2021-05-06 14:33:04.969902

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e808748ac145'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('added_time', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('update_time', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('country_code', sa.String(length=126), nullable=True),
    sa.Column('phone', sa.Integer(), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('salt', sa.String(length=128), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.Column('is_staff', sa.Boolean(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('date_joined', sa.TIMESTAMP(), nullable=True),
    sa.Column('last_login_datetime', sa.TIMESTAMP(), nullable=True),
    sa.Column('last_login_ip', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('added_time', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('update_time', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('nickname', sa.String(length=64), nullable=False),
    sa.Column('introduction', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profile')
    op.drop_table('user')
    # ### end Alembic commands ###