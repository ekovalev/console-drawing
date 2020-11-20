"""
This module contains concrete implementations of the CommandExecutor interface.
"""

from traits import CommandExecutor, Canvas
from primitives import Command
from functools import reduce


def is_int(c) -> bool:
    try:
        int(c)
    except ValueError as e:
        return False
    return True


class IdentityExecutor(CommandExecutor):
    def execute(self, canvas: Canvas, command: Command):
        return 0


class SyncCommandExecutor(CommandExecutor):
    def execute(self, canvas: Canvas, command: Command):
        if not canvas.created() and command.keyword != Command.Keyword.CREATE:
            raise ValueError('Canvas must first be created')

        if command.keyword == Command.Keyword.CREATE:
            if len(command.args) < 2:
                raise ValueError('Insufficient number of arguments')
            typecheck = reduce(lambda a, b: a and is_int(b), command.args)
            if not typecheck:
                raise TypeError('Arguments must be of type int')
            canvas.create(width=int(command.args[0]), height=int(command.args[1]))
            return 0

        if command.keyword == Command.Keyword.LINE:
            if len(command.args) < 4:
                raise ValueError('Insufficient number of arguments')
            typecheck = reduce(lambda a, b: a and is_int(b), command.args)
            if not typecheck:
                raise TypeError('Arguments must be of type int')
            canvas.draw('line', *list(map(int, command.args)))
            return 0

        if command.keyword == Command.Keyword.RECT:
            if len(command.args) < 4:
                raise ValueError('Insufficient number of arguments')
            typecheck = reduce(lambda a, b: a and is_int(b), command.args)
            if not typecheck:
                raise TypeError('Arguments must be of type int')
            canvas.draw('rect', *list(map(int, command.args)))
            return 0

        if command.keyword == Command.Keyword.FILL:
            if len(command.args) < 3:
                raise ValueError('Insufficient number of arguments')
            try:
                x = int(command.args[0])
                y = int(command.args[1])
            except ValueError as e:
                raise TypeError('First two arguments must be of type int')
            color = command.args[2]
            if len(color) > 1:
                raise ValueError('Color symbol must be a single character')
            canvas.fill(x=x, y=y, color=color)
            return 0


class AsyncCommandExecutor(CommandExecutor):
    def execute(self, canvas: Canvas, command: Command):
        pass
