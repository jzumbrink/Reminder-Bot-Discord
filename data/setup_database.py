# Use file to initialise the data base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, DATETIME, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db.sqlite', echo=True)

Base = declarative_base()


class Reminder(Base):
    __tablename__ = 'reminders'

    id = Column(Integer, primary_key=True)
    remind_time = Column(DATETIME)
    creation_time = Column(DATETIME)
    remind_msg = Column(String)
    reminded = Column(Boolean)
    completed = Column(Boolean)
    discord_data_id = Column(Integer)


class ReminderDiscordData(Base):
    __tablename__ = 'reminders_dc_data'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    channel_id = Column(Integer)


Base.metadata.create_all(engine)

