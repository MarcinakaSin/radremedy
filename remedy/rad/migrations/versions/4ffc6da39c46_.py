"""empty message

Revision ID: 4ffc6da39c46
Revises: 41196e2dde70
Create Date: 2014-07-19 20:59:51.569783

"""

# revision identifiers, used by Alembic.
revision = '4ffc6da39c46'
down_revision = '41196e2dde70'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('resource', sa.Column('visible', sa.Boolean(), nullable=True))
    op.drop_column('resource', 'visable')

    op.drop_column('resource', 'last_updated')
    op.drop_column('resource', 'date_created')

    op.add_column('resource', sa.Column('date_created', sa.DateTime(), nullable=True))
    op.add_column('resource', sa.Column('last_updated', sa.DateTime(), nullable=True))

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('resource', sa.Column('visable', sa.BOOLEAN(), nullable=True))
    op.drop_column('resource', 'visible')

    op.drop_column('resource', 'last_updated')
    op.drop_column('resource', 'date_created')

    op.add_column('resource', sa.Column('date_created', sa.Date(), nullable=True))
    op.add_column('resource', sa.Column('last_updated', sa.Date(), nullable=True)

    ### end Alembic commands ###
