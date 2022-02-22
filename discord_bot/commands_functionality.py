import discord
from data.database_operations import get_all_open_reminders_by_author, get_all_open_reminders

help_msg = """
Here is a list of the most useful commands!
```
++help
++edit <id> -t <time> -m <msg>
++list
```
Thank you for using Reminder Bot
"""


async def help_message(msg: discord.Message, args: dict):
    await msg.channel.send(help_msg)


async def list_reminders(msg: discord.Message, args: dict):
    all_open_reminders = get_all_open_reminders_by_author(author_id=msg.author.id)
    all_open_reminders = get_all_open_reminders()
    print(all_open_reminders)
    # TODO display all open reminder from this author
    for open_reminder in all_open_reminders:
        print(open_reminder)
        await msg.channel.send(open_reminder.id, open_reminder.remind_msg)