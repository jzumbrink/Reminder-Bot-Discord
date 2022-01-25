from data.models import Reminder
from data.database_operations import commit_session
import discord


async def remind(client: discord.Client, reminder: Reminder):
    reminder_channel: discord.TextChannel = client.get_channel(reminder.channel_id)
    await reminder_channel.send("Reminder " + reminder.remind_msg)

    # set the Reminder to reminded
    reminder.reminded = True
    commit_session()
