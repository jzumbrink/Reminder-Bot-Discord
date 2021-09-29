import discord, re


async def create_new_reminder(msg: discord.Message, bot_mention: str):
    msg_content = re.sub(bot_mention, '', msg.content)
    # TODO check for specified time formats used
    print(msg_content)
