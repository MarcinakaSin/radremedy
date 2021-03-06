"""empty message

Revision ID: 485bd04a12e1
Revises: 6a5adbaaf49
Create Date: 2014-07-12 21:29:44.810475

"""

# revision identifiers, used by Alembic.
revision = '485bd04a12e1'
down_revision = '6a5adbaaf49'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('city', sa.UnicodeText(), nullable=True))
    op.add_column('user', sa.Column('state', sa.Unicode(length=2), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'state')
    op.drop_column('user', 'city')
    ### end Alembic commands ###
