"""
This module contains concrete implementations of the Canvas interface.
It represent the entire application state - a concole-printable drawing canvas.

Concrete representation of the grid is up to each implementation.
"""

from __future__ import annotations
from typing import List
from traits import Canvas
import numpy as np

ASCII_WHITESPACE = 32
ASCII_X = 120

class MemoryLessCanvas(Canvas):
    def __init__(self):
        self.data: np.array = np.asarray([], dtype='uint8')


    @property
    def width(self) -> int:
        """
        Canvas width getter
        """
        return self.data.shape[1]


    @property
    def height(self) -> int:
        """
        Canvas height getter
        """
        return self.data.shape[0]


    def create(self, width: int, height: int):
        self.data = np.zeros((height, width), dtype='uint8') + ASCII_WHITESPACE


    def created(self) -> bool:
        return self.data.size != 0


    def clear(self):
        shape = self.data.shape
        self.data = np.zeros(shape, dtype='uint8') + ASCII_WHITESPACE


    def to_string(self) -> str:
        (h, w) = self.data.shape
        bar = ''
        for i in range(w + 2):
            bar += '-'

        def f(l: List) -> str:
            return '|' + ''.join(list(map(lambda x: chr(x), l))) + '|' + '\n'

        return bar + '\n' + ''.join(list(map(f, self.data.tolist()))) + bar


    def draw(self, shape, *argv):
        if shape == 'line':
            return self.draw_line(*argv)
        if shape == 'rect':
            return self.draw_rect(*argv)


    def draw_line(self, *argv):
        if len(argv) < 4:
            return
        (h, w) = self.data.shape
        x1 = argv[0]
        y1 = argv[1]
        x2 = argv[2]
        y2 = argv[3]

        # Check if the line is either horizontal or vertical, throw exception otherwise
        if not (x1 == x2 or y1 == y2):
            raise ValueError('Only horizontal or vertical lines are currently supported, try again')

        # Check if the line is horizontal and can potentially cross the visible area
        if y1 == y2 and 0 < y1 <= h:
            y = y1 - 1                  # switch from 1-based to 0-based indexing
            left = min(x1, x2) - 1      # switch from 1-based to 0-based indexing
            right = max(x1, x2)
            if right < 0 or left >= w:
                # Line doesn't intersect with the visible area
                return
            # Crop line segments outside of the visible area
            left = max(left, 0)
            right = min(right, w)
            for j in range(left, right):
                self.data[y][j] = ASCII_X

        # Check if the line is vertical and can be draw (at least partially)
        if x1 == x2 and 0 < x1 <= w:
            x = x1 - 1                  # switch from 1-based to 0-based indexing
            top = min(y1, y2) - 1       # switch from 1-based to 0-based indexing
            bottom = max(y1, y2)
            if bottom < 0 or top >= h:
                # Line doesn't intersect with the visible area
                return
            # Crop line segments outside of the visible area
            top = max(top, 0)
            bottom = min(bottom, h)
            for i in range(top, bottom):
                self.data[i][x] = ASCII_X


    def draw_rect(self, *argv):
        if len(argv) < 4:
            return
        (h, w) = self.data.shape
        x1 = argv[0]
        y1 = argv[1]
        x2 = argv[2]
        y2 = argv[3]

        # Check if the provided coordinates are consistent
        if x1 > x2 or y1 > y2:
            raise ValueError('Rectangle must have a non-negative area, try again')

        # Check if the rect has intersection with the visible area of the canvas, if not - return without error
        if x1 > w or x2 <= 0 or y1 > h or y2 <= 0:
            return

        self.draw_line(x1, y1, x2, y1)
        self.draw_line(x2, y1, x2, y2)
        self.draw_line(x2, y2, x1, y2)
        self.draw_line(x1, y2, x1, y1)


    def fill(self, x: int, y: int, color: str):
        (h, w) = self.data.shape

        # If the base point is outside the visible area simply return
        if not (0 < x <= w and 0 < y <= h):
            return

        c = ord(color)
        x -= 1  # Convert to 0-based coordinates
        y -= 1  # Convert to 0-based coordinates

        # If the current color of the base point matches the new color we just return
        if self.data[y][x] == c:
            return

        self._paint_neighbours(x, y, self.data[y][x], c, np.zeros_like(self.data, dtype='uint8'))


    def _paint_neighbours(self, x: int, y: int, old_color: int, new_color: int, visited: np.array):
        """
        Auxiliary method called recursively to paint the immediate neighbours of a point
        No arguments boundary checks required here (all done in calling method)
        :param x: x coordinate
        :param y: y coordinate
        :param old_color: point color before repainting
        :param new_color: point new color
        :param visited: np.array of the same shape as the canvas that tracks visited points
        """
        (h, w) = self.data.shape

        self.data[y][x] = new_color
        visited[y][x] = True

        # Check the point to the left
        if x > 0 and (not visited[y][x - 1]) \
                and (self.data[y][x - 1] == old_color or self.data[y][x - 1] == new_color):
            self._paint_neighbours(x - 1, y, old_color, new_color, visited)

        # Check the point above
        if y > 0 and (not visited[y - 1][x]) \
                and (self.data[y - 1][x] == old_color or self.data[y - 1][x] == new_color):
            self._paint_neighbours(x, y - 1, old_color, new_color, visited)

        # Check the point to the right
        if x < w - 1 and (not visited[y][x + 1]) \
                and (self.data[y][x + 1] == old_color or self.data[y][x + 1] == new_color):
            self._paint_neighbours(x + 1, y, old_color, new_color, visited)

        # Check the point below
        if y < h - 1 and (not visited[y + 1][x]) \
                and (self.data[y + 1][x] == old_color or self.data[y + 1][x] == new_color):
            self._paint_neighbours(x, y + 1, old_color, new_color, visited)
