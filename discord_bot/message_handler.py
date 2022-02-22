import discord, json
from .commands_structure import CommandTypes
from .commands import root
from .pattern import is_pattern_valid
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


def get_command_name_and_args(msg_content: str):
    possible_commands = [root]

    while len(possible_commands) > 0:
        # search for the command
        current_command = possible_commands.pop(0)

        if current_command.type == CommandTypes.collection:
            possible_commands += current_command.childs
        elif current_command.type == CommandTypes.single_command:
            result_args = is_pattern_valid(current_command, msg_content)
            if result_args is not None:
                return {
                    'command': current_command,
                    'args': result_args
                }
        else:
            raise TypeError


async def on_message(msg: discord.Message, client: discord.Client):
    if text_starts_with_command_prefixes(msg.content):
        msg_content = get_text_without_prefixes(msg.content)
        command_and_args = get_command_name_and_args(msg_content)
        if command_and_args is None:
            await send_error_message(msg.channel, "Wrong command usage")
        else:
            # Execute command and provide args
            await command_and_args['command'].execute(msg, command_and_args['args'])
    else:
        if is_bot_mentioned(client, msg.content):
            await create_new_reminder(msg, get_bot_mention(client))

