import enum
from abc import ABC, abstractmethod


class Command(ABC):
    name: str
    pattern: str


class CommandCollection(Command):
    childs: list

    def __init__(self, name, pattern):
        self.name = name
        self.pattern = pattern
        self.childs = []

    def add_child(self, command: Command):
        self.childs.append(command)

    def add_childs(self, *args: Command):
        for arg in args:
            self.add_child(arg)

class SingleCommand(Command):

    def __init__(self, name, pattern):
        self.name = name
        self.pattern = pattern

    def execute(self, full_specific_command):
        pass


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
    pattern="edit <id> -t(new_time)"
)

edit_message_cmd = SingleCommand(
    name="edit-message",
    pattern="edit <id> -m(new_msg)"
)

edit_collection.add_childs(edit_r_time_cmd, edit_message_cmd)

root.add_child(edit_collection)

print()