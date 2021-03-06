import discord, json

from discord_bot import message_handler, start_discord_bot

client = discord.Client()

with open('discord_config.json', 'r') as config_dc_file:
    config_dc = json.loads(config_dc_file.read())


@client.event
async def on_message(msg):
    if msg.author.id == client.user.id:
        return

    await message_handler.on_message(msg, client)


@client.event
async def on_ready():

    await start_discord_bot.on_ready(client)


client.run(config_dc['discord-token'])
