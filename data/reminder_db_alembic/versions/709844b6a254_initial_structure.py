"""initial structure

Revision ID: 709844b6a254
Revises: 
Create Date: 2021-09-29 11:53:43.056429

"""
from alembic import op
from sqlalchemy import Column, Integer, DATETIME, String, Boolean


# revision identifiers, used by Alembic.
revision = '709844b6a254'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'reminders',
        Column('id', Integer, primary_key=True),
        Column('remind_time', DATETIME),
        Column('creation_time', DATETIME),
        Column('remind_msg', String),
        Column('completed', Boolean),
        Column('reminded', Boolean),
        Column('discord_data_id', Integer),
    )

    op.create_table(
        'reminders_discord_specific_data',
        Column('id', Integer, primary_key=True),
        Column('user_id', Integer),
        Column('channel_id', Integer)
    )


def downgrade():
    op.drop_table('reminders')
    op.drop_table('reminders_discord_specific_data')
