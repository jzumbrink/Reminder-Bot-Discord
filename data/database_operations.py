from sqlalchemy import insert, create_engine
from .models import Reminder
import datetime
import discord

engine = create_engine('sqlite:///db.sqlite', echo=True)

connection = engine.connect()


def add_reminder(remind_msg: str, remind_time, msg: discord.Message):
    connection.execute(
        insert(Reminder).values(
            remind_msg=remind_msg,
            remind_time=remind_time,
            creation_time=datetime.datetime.now(),
            reminded=False,
            author_id=msg.author.id,
            channel_od=msg.channel.id,
        )
    )
    connection.commit()
