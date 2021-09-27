# Use file to initialise the data base
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, Integer, DATETIME, String, Boolean

engine = create_engine('sqlite:///db.sqlite', echo=True)

meta = MetaData()

reminders = Table(
    'reminders', meta,
    Column('id', Integer, primary_key=True),
    Column('remind_time', DATETIME),
    Column('creation_time', DATETIME),
    Column('remind_msg', String),
    Column('completed', Boolean),
    Column('reminded', Boolean),
    Column('discord_data_id', Integer)
)

reminders_dc_data = Table(
    'reminders_discord_specific_data', meta,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer),
    Column('channel_id', Integer)
)

meta.create_all(engine)