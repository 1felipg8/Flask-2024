"""empty message

Revision ID: 914ef9906dab
Revises: b8883f6240c9
Create Date: 2024-05-23 09:15:10.786158

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '914ef9906dab'
down_revision = 'b8883f6240c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_comentarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data_criacao', sa.DateTime(), nullable=True),
    sa.Column('comentario', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('comentario')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comentario',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('texto', sa.VARCHAR(), nullable=False),
    sa.Column('data', sa.DATETIME(), nullable=True),
    sa.Column('post_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('post_comentarios')
    # ### end Alembic commands ###
