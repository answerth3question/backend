"""empty message

Revision ID: 26e760e290e4
Revises: 3f7406e5226a
Create Date: 2019-08-23 09:04:37.942125

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '26e760e290e4'
down_revision = '3f7406e5226a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_login',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ts', postgresql.TIMESTAMP(), server_default=sa.text("timezone('utc', now())"), nullable=True),
    sa.Column('user_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_login')
    # ### end Alembic commands ###
