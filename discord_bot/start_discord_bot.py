import discord, json

with open('discord_config.json', 'r') as config_dc_file:
    config_dc = json.loads(config_dc_file.read())


async def on_ready(client: discord.Client):
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-' * 15)

    activity = discord.Activity(type=discord.ActivityType.watching, name=config_dc['bot-activity-content'])
    await client.change_presence(status=discord.Status.online,
                                 activity=activity)
