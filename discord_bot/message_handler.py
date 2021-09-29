import discord, json
from .commands import get_command_name_and_args

async def send_error_message(channel: discord.TextChannel, message: str):
    await channel.send(message)

def text_starts_with_command_prefixes(text: str) -> bool:
    for prefix in config_dc['command-prefixes']:
        if text.startswith(prefix):
            return True
    return False


def get_text_without_prefixes(text: str) -> str:
    for prefix in config_dc['command-prefixes']:
        if text.startswith(prefix):
            return text[len(prefix):]

with open('discord_config.json', 'r') as config_dc_file:
    config_dc = json.loads(config_dc_file.read())

with open('discord_bot/error_messages.json', 'r') as error_msg_file:
    error_msg = json.loads(error_msg_file.read())


async def on_message(msg: discord.Message):
    if text_starts_with_command_prefixes(msg.content):
        msg_content = get_text_without_prefixes(msg.content)
        command_and_args = get_command_name_and_args(msg_content)
        if command_and_args is None:
            await send_error_message(msg.channel, "Wrong command usage")
        else:
            # TODO Command ausführen
            pass
