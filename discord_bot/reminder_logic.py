import discord, re
from datetime_handling.datetime_handling import extract_time_shortcuts, extract_explizit_time_specification, add_time_shortcuts_to_datetime

from data.database_operations import add_reminder


async def create_new_reminder(msg: discord.Message, bot_mention: str):
    msg_content = re.sub(bot_mention, '', msg.content)

    clear_msg, remind_time = extract_explizit_time_specification(text=msg_content)
    clear_msg, time_shortcuts = extract_time_shortcuts(clear_msg)
    remind_time = add_time_shortcuts_to_datetime(time_shortcuts, remind_time)

    clear_msg = clear_msg.strip()

    add_reminder(clear_msg, remind_time, msg)

    await msg.channel.send(f"Reminder created for {remind_time} with message: {clear_msg}")
