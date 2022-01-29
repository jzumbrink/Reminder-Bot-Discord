import time

import discord

from data.database_operations import get_all_open_reminders
from .existent_reminder_manager import remind


async def reminder_loop(client: discord.Client):
    t1 = time.time()

    while True:
        print("wtf2")
        open_reminders = get_all_open_reminders()
        print("Hi")
        print(open_reminders)
        for open_reminder in open_reminders:
            print(open_reminder.id, open_reminder.author_id)
            await remind(client, open_reminder)
        time.sleep(2)


async def on_ready(client: discord.Client):
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-' * 15)

    while True:
        try:
            await reminder_loop(client)
        except:
            # con error
            time.sleep(3)
