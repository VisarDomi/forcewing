"""empty message

Revision ID: 8bf90a32a0a6
Revises: 
Create Date: 2019-01-10 15:53:17.671023

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bf90a32a0a6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('name_lower_case', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('image_file', sa.String(length=100), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('blogs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=True),
    sa.Column('title', sa.String(length=1000), nullable=True),
    sa.Column('subtitle', sa.String(length=1000), nullable=True),
    sa.Column('section_title', sa.String(length=3000), nullable=True),
    sa.Column('section_content', sa.Text(), nullable=True),
    sa.Column('subsection_title', sa.String(length=3000), nullable=True),
    sa.Column('subsection_content', sa.Text(), nullable=True),
    sa.Column('quote', sa.String(length=1000), nullable=True),
    sa.Column('category', sa.String(length=100), nullable=True),
    sa.Column('image_file', sa.String(length=100), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('portfolios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=True),
    sa.Column('title', sa.String(length=1000), nullable=True),
    sa.Column('subtitle', sa.String(length=1000), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('tag', sa.String(length=100), nullable=True),
    sa.Column('client_logo', sa.String(length=100), nullable=True),
    sa.Column('client_name', sa.String(length=100), nullable=True),
    sa.Column('website', sa.String(length=1000), nullable=True),
    sa.Column('main_image', sa.String(length=1000), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('portfolioimages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=100), nullable=True),
    sa.Column('portfolio_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['portfolio_id'], ['portfolios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('portfolioimages')
    op.drop_table('portfolios')
    op.drop_table('blogs')
    op.drop_table('users')
    op.drop_table('tags')
    op.drop_table('categories')
    # ### end Alembic commands ###
