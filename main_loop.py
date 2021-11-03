import discord, json

from discord_reminder_loop import start_reminder_loop

client = discord.Client()

with open('discord_config.json', 'r') as config_dc_file:
    config_dc = json.loads(config_dc_file.read())


@client.event
async def on_ready():
    await start_reminder_loop.on_ready(client)


client.run(config_dc['discord-token'])
