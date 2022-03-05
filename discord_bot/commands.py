from .commands_structure import *
from .commands_functionality import *

root = CommandCollection(
    name="root-collection",
    pattern="#"
)

edit_cmd = SingleCommand(
    name="edit",
    pattern="edit <id>",
    func=None,
    allowed_args=[
        CommandArgument(
            name="time",
            short_arg='t',
            long_arg="time",
        ),
        CommandArgument(
            name="message",
            short_arg='m',
            long_arg="message",
        ),
    ]
)

help_cmd = SingleCommand(
    name="help",
    pattern="help",
    func=help_message,
)

list_reminders_cmd = SingleCommand(
    name="list",
    pattern="list",
    func=list_reminders,
)

details_reminder_cmd = SingleCommand(
    name="details",
    pattern="details <id>",
    func=details_reminder,
)

root.add_child(edit_cmd)
root.add_child(help_cmd)
root.add_child(list_reminders_cmd)
root.add_child(details_reminder_cmd)
