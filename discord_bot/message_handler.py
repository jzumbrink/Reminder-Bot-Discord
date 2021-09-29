import discord, json

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


async def get_command_from_msg_content(msg_content: str) -> str:
    if len(msg_content) == 0:
        await send_error_message(error_msg['command-size-null'])
        return None
    if

with open('../discord_config.json', 'r') as config_dc_file:
    config_dc = json.loads(config_dc_file.read())

with open('error_messages.json', 'r') as error_msg_file:
    error_msg = json.loads(error_msg_file.read())


async def on_message(msg: discord.Message):
    if text_starts_with_command_prefixes(msg.content):
        msg_content = get_text_without_prefixes(msg.content)
        command = await get_command_from_msg_content(msg_content)
        if command is not None:
