import discord, json
from .commands_structure import get_command_name_and_args
from .reminder_logic import create_new_reminder


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


def get_bot_mention(client: discord.Client):
    return f'<@!{client.user.id}>'


def is_bot_mentioned(client: discord.Client, text: str) -> bool:
    return get_bot_mention(client) in text


with open('discord_config.json', 'r') as config_dc_file:
    config_dc = json.loads(config_dc_file.read())

with open('discord_bot/error_messages.json', 'r') as error_msg_file:
    error_msg = json.loads(error_msg_file.read())


async def on_message(msg: discord.Message, client: discord.Client):
    if text_starts_with_command_prefixes(msg.content):
        msg_content = get_text_without_prefixes(msg.content)
        command_and_args = get_command_name_and_args(msg_content)
        if command_and_args is None:
            await send_error_message(msg.channel, "Wrong command usage")
        else:
            # TODO Command ausführen
            pass
    else:
        if is_bot_mentioned(client, msg.content):
            await create_new_reminder(msg, get_bot_mention(client))

