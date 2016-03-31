"""empty message

Revision ID: 33b8a933f733
Revises: None
Create Date: 2015-03-10 13:12:58.195575

"""

# revision identifiers, used by Alembic.
revision = '33b8a933f733'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('profile')
    op.drop_table('book')
    op.drop_table('profileDB')
    op.add_column('myprofile', sa.Column('nickname', sa.String(length=80), nullable=True))
    op.create_unique_constraint(None, 'myprofile', ['nickname'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'myprofile', type_='unique')
    op.drop_column('myprofile', 'nickname')
    op.create_table('profileDB',
    sa.Column('id', sa.INTEGER(), server_default=sa.text(u'nextval(\'"profileDB_id_seq"\'::regclass)'), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'profileDB_pkey')
    )
    op.create_table('book',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('author', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(length=40), autoincrement=False, nullable=False),
    sa.Column('publication_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'book_pkey')
    )
    op.create_table('profile',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('sex', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('image', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'profile_pkey')
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'user_pkey')
    )
    ### end Alembic commands ###
