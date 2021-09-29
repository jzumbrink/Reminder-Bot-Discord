import enum
from abc import ABC
from .pattern import is_pattern_valid


class CommandTypes(enum.Enum):
    clt = 0
    cmd = 1


class Command(ABC):
    name: str
    pattern: str
    type: CommandTypes


class CommandCollection(Command):
    childs: list

    def __init__(self, name, pattern):
        self.name = name
        self.pattern = pattern
        self.childs = []
        self.type = CommandTypes.clt

    def add_child(self, command: Command):
        self.childs.append(command)

    def add_childs(self, *args: Command):
        for arg in args:
            self.add_child(arg)


class SingleCommand(Command):

    def __init__(self, name, pattern):
        self.name = name
        self.pattern = pattern
        self.type = CommandTypes.cmd


root = CommandCollection(
    name="root-collection",
    pattern="#"
)

edit_collection = CommandCollection(
    name="edit-collection",
    pattern="edit <id> #"
)

edit_r_time_cmd = SingleCommand(
    name="edit-remind-time",
    pattern="edit <id> -t"
)

edit_message_cmd = SingleCommand(
    name="edit-message",
    pattern="edit <id> -m"
)

edit_collection.add_childs(edit_r_time_cmd, edit_message_cmd)

root.add_child(edit_collection)

print()


def get_command_name_and_args(msg_content: str):
    possible_commands = [root]

    while len(possible_commands) > 0:
        # search for the command
        current_command = possible_commands.pop(0)

        if current_command.type == CommandTypes.clt:
            possible_commands += current_command.childs
        elif current_command.type == CommandTypes.cmd:
            result = is_pattern_valid(current_command.pattern, msg_content)
            if result is not None:
                return {
                    'name': current_command.name,
                    'args': result
                }
        else:
            raise TypeError

