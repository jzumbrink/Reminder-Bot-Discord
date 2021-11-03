from sqlalchemy import insert, create_engine, select
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
    print("was")

    result = session.execute(
        select(Reminder)#.where(Reminder.remind_time < datetime.datetime.now() and not Reminder.reminded)
    )

    print()