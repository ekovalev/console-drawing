"""

This module introduces the interfaces that, in turn, represent the concepts and abstractions
the application operates on.

"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

from primitives import Command


class Canvas(ABC):
    """
    The application state.
    """

    @abstractmethod
    def create(self, width: int, height: int):
        """
        Create canvas or reset canvas dimensions and data
        :param width: canvas width
        :param height: canvas height
        :return:
        """
        pass

    @abstractmethod
    def clear(self):
        """
        Clear canvas contents without resizing
        :return:
        """
        pass

    @abstractmethod
    def to_string(self) -> str:
        """
        Serialize canvas contents into string
        :return: serialized canvas contents
        """
        pass

    @abstractmethod
    def draw(self, *argv):
        """
        General drawing method; the first argument denotes the concrete shape to draw
        :param argv: [shape, coordinate, color]
        :return:
        """
        pass

    @abstractmethod
    def fill(self, x: int, y: int, color: str):
        """
        Bucket fill method
        :param x: x coordinate of the base point
        :param y: y coordinate of the base point
        :param color: fill color - a 1-length str
        :return:
        """
        pass

    @abstractmethod
    def created(self) -> bool:
        """
        Checks if the canvas has dimensions (the create() method has been called)
        :return: True if the canvas has dimensions, False otherwise
        """


class Writer(ABC):
    """
    Interface representing a console writer for the Canvas application to print out the app state.

    Concrete implementations may include variants ranging from simple console printing to
    more sophisticated version with ASCII animaion etc.
    """

    @abstractmethod
    def write(self, data: str):
        pass


class CommandExecutor(ABC):
    """
    Abstract class representing a concept of a command processor.

    Takes a tuple (canvas, command), validates the command against the canvas and produces a
     potentially new canvas.
    """

    @abstractmethod
    def execute(self, canvas: Canvas, command: Command) -> int:
        pass
