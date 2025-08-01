from services import TaskService
from argparse import ArgumentParser
from typing import Callable
import sys


def main():

    supported_queries: dict[str,dict] = get_supported_queries()

    querie, args = get_querie(supported_queries)

    try:
        querie(**args)
    except KeyError:
        sys.exit("No task found with the provided ID")


def get_supported_queries() -> dict[str, dict]:
    return {
        "add": {
            "target": TaskService.add_task,
            "help": "Add a new task to your task list",
            "args": [
                {"name_or_flags": ["description"], "help": "Description of the task"}
            ],
        },
        "delete": {
            "target": TaskService.delete_task,
            "help": "Delete a task from your task list",
            "args": [
                {
                    "name_or_flags": ["id"],
                    "help": "ID of the task you want to delete",
                }
            ],
        },
        "update": {
            "target": TaskService.update_task,
            "help": "Update the description of a task",
            "args": [
                {
                    "name_or_flags": ["id"],
                    "help": "ID of the task to update",
                },
                {
                    "name_or_flags": ["description"],
                    "help": "New description for the task",
                },
            ],
        },
        "list": {
            "target": TaskService.list_tasks,
            "help": "List all tasks or filter them by status",
            "args": [
                {
                    "name_or_flags": ["--status", "-s"],
                    "help": "Filter tasks by status (default is 'all')",
                    "choices": ["all", "done", "todo", "in-progress"],
                    "type": str.lower,
                    "default": "all",
                }
            ],
        },
        "mark-in-progress": {
            "target": TaskService.mark_as_in_progress,
            "help": "Mark a task as 'in-progress'",
            "args": [
                {
                    "name_or_flags": ["id"],
                    "help": "ID of the task",
                },
                ]
        },
        "mark-done": {
            "target": TaskService.mark_as_done,
            "help": "Mark a task as 'done'",
            "args": [
                {
                    "name_or_flags": ["id"],
                    "help": "ID of the task",
                }],
        },
    }

def get_querie(supported_queries: dict[str, dict]) -> tuple[Callable, dict]:
    parser: ArgumentParser = ArgumentParser(
        description="A CLI application to efficiently manage your tasks"
    )
    sub_parsers = parser.add_subparsers(title="commands", dest="command", required=True)

    for name, properties in supported_queries.items():
        p = sub_parsers.add_parser(name, help=properties["help"])
        for arg in properties["args"]:
            p.add_argument(*arg.pop("name_or_flags"), **arg)

    args: dict = parser.parse_args().__dict__
    querie: Callable = supported_queries[args.pop("command")]["target"]

    return querie, args

if __name__ == "__main__":

    main()