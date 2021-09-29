import discord, re, datetime

time_periods = {
    'year': 'y',
    'month': 'm',
    'week': 'w',
    'day': 'd',
    'hour': 'h',
    'minute': 'min',
    'second': 's'
}

time_formats = {

}



async def create_new_reminder(msg: discord.Message, bot_mention: str):
    msg_content = re.sub(bot_mention, '', msg.content)
    # TODO check for specified time formats used
    print(msg_content)
