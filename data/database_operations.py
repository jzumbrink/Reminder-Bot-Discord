from sqlalchemy import insert, create_engine, select, not_, and_, desc
from sqlalchemy.orm import sessionmaker
from .models import Reminder
import datetime
import discord

engine = create_engine('sqlite:///data/db.sqlite', echo=True)

connection = engine.connect()

reminder_table = Reminder.__table__

Session = sessionmaker(bind=engine)
session = Session()


def add_reminder(remind_msg: str, remind_time, msg: discord.Message) -> bool:
    connection.execute(
        insert(Reminder).values(
            remind_msg=remind_msg,
            remind_time=remind_time,
            creation_time=datetime.datetime.now(),
            reminded=False,
            author_id=msg.author.id,
            channel_id=msg.channel.id,
        )
    )

    return True


def get_all_open_reminders():
    return session.query(Reminder).filter(and_(Reminder.remind_time < datetime.datetime.now(), not_(Reminder.reminded)))


def get_all_open_reminders_by_author(author_id: int):
    return session.query(Reminder).filter(and_(not_(Reminder.reminded), Reminder.author_id == author_id)).order_by(Reminder.remind_time)


def get_reminder_by_user_specific_id(user_specific_id: int):
    pass


def commit_session():
    session.commit()
