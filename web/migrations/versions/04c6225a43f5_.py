"""empty message

Revision ID: 04c6225a43f5
Revises: 56b21e4e1038
Create Date: 2019-09-03 15:30:49.108509

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '04c6225a43f5'
down_revision = '56b21e4e1038'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_content',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('text', sa.String(length=1000), nullable=False),
    sa.Column('user_post_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['user_post_id'], ['user_post.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('post_review', sa.Column('user_post_id', postgresql.UUID(as_uuid=True), nullable=False))
    op.create_foreign_key(None, 'post_review', 'user_post', ['user_post_id'], ['id'])
    op.drop_column('post_review', 'post_id')
    op.add_column('user_post', sa.Column('post_prompt_id', postgresql.UUID(as_uuid=True), nullable=False))
    op.add_column('user_post', sa.Column('status', sa.Integer(), nullable=True))
    op.drop_constraint('user_post_status_id_fkey', 'user_post', type_='foreignkey',)
    op.drop_constraint('user_post_prompt_id_fkey', 'user_post', type_='foreignkey')
    op.create_foreign_key(None, 'user_post', 'post_prompt', ['post_prompt_id'], ['id'])
    op.drop_column('user_post', 'status_id')
    op.drop_column('user_post', 'content')
    op.drop_column('user_post', 'prompt_id')
    op.drop_table('post_status')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_post', sa.Column('prompt_id', postgresql.UUID(), autoincrement=False, nullable=False))
    op.add_column('user_post', sa.Column('content', sa.VARCHAR(length=1000), autoincrement=False, nullable=False))
    op.add_column('user_post', sa.Column('status_id', postgresql.UUID(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'user_post', type_='foreignkey')
    op.create_foreign_key('user_post_prompt_id_fkey', 'user_post', 'post_prompt', ['prompt_id'], ['id'])
    op.create_foreign_key('user_post_status_id_fkey', 'user_post', 'post_status', ['status_id'], ['id'], ondelete='CASCADE')
    op.drop_column('user_post', 'status')
    op.drop_column('user_post', 'post_prompt_id')
    op.add_column('post_review', sa.Column('post_id', postgresql.UUID(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'post_review', type_='foreignkey')
    op.drop_column('post_review', 'user_post_id')
    op.create_table('post_status',
    sa.Column('id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('status', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='post_status_pkey')
    )
    op.drop_table('post_content')
    # ### end Alembic commands ###