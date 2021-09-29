"""changed to autogeneration

Revision ID: 72834fecd6ef
Revises: 709844b6a254
Create Date: 2021-09-29 21:27:54.114456

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '72834fecd6ef'
down_revision = '709844b6a254'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reminder',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('remind_msg', sa.String(), nullable=True),
                    sa.Column('remind_time', sa.DATETIME(), nullable=True),
                    sa.Column('creation_time', sa.DATETIME(), nullable=True),
                    sa.Column('reminded', sa.Boolean(), nullable=True),
                    sa.Column('discord_data_id', sa.Integer(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('reminder_discord_data',
                    sa.Column('reminder_id', sa.Integer(), nullable=False),
                    sa.Column('author_id', sa.Integer(), nullable=True),
                    sa.Column('channel_id', sa.Integer(), nullable=True),
                    sa.PrimaryKeyConstraint('reminder_id')
                    )
    op.drop_table('reminders')
    op.drop_table('reminders_discord_specific_data')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reminders_discord_specific_data',
                    sa.Column('id', sa.INTEGER(), nullable=False),
                    sa.Column('user_id', sa.INTEGER(), nullable=True),
                    sa.Column('channel_id', sa.INTEGER(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('reminders',
                    sa.Column('id', sa.INTEGER(), nullable=False),
                    sa.Column('remind_time', sa.DATETIME(), nullable=True),
                    sa.Column('creation_time', sa.DATETIME(), nullable=True),
                    sa.Column('remind_msg', sa.VARCHAR(), nullable=True),
                    sa.Column('completed', sa.BOOLEAN(), nullable=True),
                    sa.Column('reminded', sa.BOOLEAN(), nullable=True),
                    sa.Column('discord_data_id', sa.INTEGER(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.drop_table('reminder_discord_data')
    op.drop_table('reminder')
    # ### end Alembic commands ###