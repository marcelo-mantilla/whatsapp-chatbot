"""empty message

Revision ID: e2623bee73ac
Revises: 
Create Date: 2023-06-01 11:53:09.052457

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2623bee73ac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('phone_number', sa.String(length=20), nullable=False),
    sa.Column('category', sa.String(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('phone_number')
    )
    op.create_table('chats',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('message', sa.String(length=1200), nullable=False),
    sa.Column('origin', sa.String(length=20), nullable=False),
    sa.Column('format', sa.String(length=20), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('sequence', sa.Integer(), nullable=False),
    sa.Column('wa_created_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('error_logs',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('traceback', sa.String(length=1000), nullable=True),
    sa.Column('chat_id', sa.UUID(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['chat_id'], ['chats.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('error_logs')
    op.drop_table('chats')
    op.drop_table('users')
    # ### end Alembic commands ###
