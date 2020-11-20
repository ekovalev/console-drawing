"""

This module contains definitions of primitive types used by the application.

"""

from __future__ import annotations
from enum import Enum
from typing import List


class Command:
    """
    A command from user that can update the application state:
    (State, Command) -> State
    """

    class Keyword(Enum):
        CREATE = 1
        LINE = 2
        RECT = 3
        FILL = 4
        QUIT = 5
        UNKNOWN = 6

    keyword: Keyword
    args: List

    def __init__(self, keyword: Keyword, *argv):
        self.keyword = keyword
        self.args = list(argv)
