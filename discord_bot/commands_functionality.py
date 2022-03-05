import discord
from data.database_operations import *

help_msg = """
Here is a list of the most useful commands!
```
++help
++edit <id> -t <time> -m <msg>
++list
```
Thank you for using Reminder Bot
"""


"""
Strucutre of args: dict
{
    "aparams": [param0, param1, ...],
    "kparams": {
        "paramX": "valueX",
        "paramY": "valueY",
        ...
    }
}
"""


async def help_message(msg: discord.Message, args: dict):
    await msg.channel.send(help_msg)


async def list_reminders(msg: discord.Message, args: dict):
    all_open_reminders = get_all_open_reminders_by_author(author_id=msg.author.id)
    for open_reminder in all_open_reminders:
        print(open_reminder)
        await msg.channel.send(f"{open_reminder.id} at {open_reminder.remind_time}: {open_reminder.remind_msg}")


async def details_reminder(msg: discord.Message, args: dict):
    reminder_id = args['aparams'][0]
    requested_reminder = get_reminder_by_user_specific_id(reminder_id)
    embed = discord.Embed(title=f"Reminder (id: {reminder_id})", description="fgdsfgdsgfd", color=0x0000ff)
    embed.add_field(name="Datetime", value="Some datetime like 2023-02-11")
    await msg.channel.send("Here are the details about your requested remidner:", embed=embed)
