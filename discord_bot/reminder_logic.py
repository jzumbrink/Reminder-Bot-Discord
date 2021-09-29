import discord, re
from datetime_handling.datetime_handling import extract_time_shortcuts, add_time_shortcuts_to_now


async def create_new_reminder(msg: discord.Message, bot_mention: str):
    msg_content = re.sub(bot_mention, '', msg.content)
    # TODO check for specified time formats used
    print(msg_content)
    clear_msg, time_shortcuts = extract_time_shortcuts(msg_content)
    remind_time = add_time_shortcuts_to_now(time_shortcuts)

    await msg.channel.send(f"Reminder created for {remind_time} with message: {clear_msg}")
