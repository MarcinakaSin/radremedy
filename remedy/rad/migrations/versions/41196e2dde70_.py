"""empty message

Revision ID: 41196e2dde70
Revises: 485bd04a12e1
Create Date: 2014-07-14 20:53:06.416557

"""

# revision identifiers, used by Alembic.
revision = '41196e2dde70'
down_revision = '485bd04a12e1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('resource', sa.Column('date_created', sa.DateTime(), nullable=True))
    op.add_column('resource', sa.Column('last_updated', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('resource', 'last_updated')
    op.drop_column('resource', 'date_created')
    ### end Alembic commands ###
