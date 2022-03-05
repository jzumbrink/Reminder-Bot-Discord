import enum, discord
from abc import ABC


class CommandTypes(enum.Enum):
    collection = 0
    single_command = 1


class Command(ABC):
    name: str
    pattern: str
    type: CommandTypes


class CommandCollection(Command):
    childs: list

    def __init__(self, name: str, pattern: str):
        self.name = name
        self.pattern = pattern
        self.childs = []
        self.type = CommandTypes.collection

    def add_child(self, command: Command):
        self.childs.append(command)

    def add_childs(self, *args: Command):
        for arg in args:
            self.add_child(arg)


class SingleCommand(Command):

    def __init__(self, name: str, pattern: str, func, allowed_args: list = []):
        self.name = name
        self.pattern = pattern
        pattern_split = self.pattern.split(' ')
        self.keyword = pattern_split[0]
        self.count_aparams = len(pattern_split) - 1
        self.type = CommandTypes.single_command
        self.func = func
        self.allowed_args = allowed_args

    async def execute(self, msg: discord.Message, arguments: dict):
        if self.func is not None:
            """
            Strucutre of arguments:
            {
                "aparams": [param0, param1, ...],
                "kparams": {
                    "paramX": "valueX",
                    "paramY": "valueY",
                    ...
                }
            }
            """
            await self.func(msg, arguments)
        else:
            raise RuntimeError


class CommandArgument:

    def __init__(self, name: str, short_arg: str, long_arg: str, expect_value: bool = True):
        self.name = name
        self.short_arg = '-' + short_arg if short_arg is not None else None
        self.long_arg = '--' + long_arg if long_arg is not None else None
        self.expect_value = expect_value
        self.type_check_func = lambda value: True

    def set_type_check_fund(self, type_check_func):
        # TODO support for type check fund
        self.type_check_func = type_check_func

    def check_if_value_provided(self, i: int, text_split: list) -> bool:
        return not self.expect_value or i+1 < len(text_split) and self.type_check_func(text_split[i+1])

    def create_specific_arg_list(self, value=None) -> list:
        return [self.name, value]

    def extract_argument_from_text(self, text_split: list) -> list:
        for i in range(len(text_split)):
            if (self.short_arg is not None and text_split[i] == self.short_arg
                    or self.long_arg is not None and text_split[i] == self.long_arg) and self.check_if_value_provided(i, text_split):
                text_split.pop(i)
                if self.expect_value:
                    return self.create_specific_arg_list(text_split.pop(i))
                return self.create_specific_arg_list()
        return None
