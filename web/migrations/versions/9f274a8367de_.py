"""empty message

Revision ID: 9f274a8367de
Revises: 26e760e290e4
Create Date: 2019-08-23 09:13:14.709221

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9f274a8367de'
down_revision = '26e760e290e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_login',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ts', postgresql.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('user_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_login')
    # ### end Alembic commands ###
