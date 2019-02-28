"""third Migration

Revision ID: 68e77ec49edf
Revises: 85c1131d645a
Create Date: 2019-02-28 10:29:06.483462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68e77ec49edf'
down_revision = '85c1131d645a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    op.drop_column('users', 'password_secure')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###
