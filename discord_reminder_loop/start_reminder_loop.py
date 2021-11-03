import time

import discord

from data.database_operations import get_all_open_reminders


async def reminder_loop():
    print("wtf")
    t1 = time.time()

    while True:
        print("wtf2")
        open_reminders = get_all_open_reminders()
        print("Hi")
        print(open_reminders)

        time.sleep(3)


async def on_ready(client: discord.Client):
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-' * 15)

    while True:
        try:
            await reminder_loop()
        except:
            # con error
            time.sleep(3)
