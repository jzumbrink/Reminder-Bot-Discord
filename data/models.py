from sqlalchemy import Column, Integer, DATETIME, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Reminder(Base):
    __tablename__ = 'reminder'
    id = Column(Integer, primary_key=True)
    remind_msg = Column(String)
    remind_time = Column(DATETIME)
    creation_time = Column(DATETIME)
    reminded = Column(Boolean)
    author_id = Column(Integer)
    channel_id = Column(Integer)
