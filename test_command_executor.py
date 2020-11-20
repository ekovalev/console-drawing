"""
Unit tests for canvas module
"""

import unittest
import numpy as np
from command_executor import SyncCommandExecutor as Executor
from canvas import MemoryLessCanvas as Canvas
from primitives import Command


class CommandExecutorTest(unittest.TestCase):
    def test_execute_before_canvas_created_throws(self):
        executor = Executor()
        canvas = Canvas()
        command = Command(Command.Keyword.LINE, 1, 4, 10, 4)
        self.assertRaises(ValueError, executor.execute, canvas, command)

    def test_execute_creat_ok(self):
        executor = Executor()
        canvas = Canvas()
        command = Command(Command.Keyword.CREATE, 10, 4)
        expected = np.zeros((4, 10), dtype='uint8') + 32
        executor.execute(canvas, command)
        self.assertTrue((canvas.data == expected).all())

    def test_execute_create_wrong_args_num_throws(self):
        executor = Executor()
        canvas = Canvas()
        command = Command(Command.Keyword.CREATE, 10)
        self.assertRaises(ValueError, executor.execute, canvas, command)

    def test_execute_create_wrong_types_throws(self):
        executor = Executor()
        canvas = Canvas()
        command = Command(Command.Keyword.CREATE, 10, 'str')
        self.assertRaises(TypeError, executor.execute, canvas, command)

    def test_execute_line_ok(self):
        executor = Executor()
        canvas = Canvas()
        canvas.create(8, 4)
        command = Command(Command.Keyword.LINE, 2, 4, 7, 4)
        self.assertEqual(executor.execute(canvas, command), 0)

    def test_execute_line_wrong_args_num_throws(self):
        executor = Executor()
        canvas = Canvas()
        canvas.create(8, 4)
        command = Command(Command.Keyword.LINE, 1, 4, 10)
        self.assertRaises(ValueError, executor.execute, canvas, command)

    def test_execute_line_wrong_types_throws(self):
        executor = Executor()
        canvas = Canvas()
        canvas.create(8, 4)
        command = Command(Command.Keyword.LINE, 1, 4, 10, 'str')
        self.assertRaises(TypeError, executor.execute, canvas, command)

    def test_execute_rect_ok(self):
        executor = Executor()
        canvas = Canvas()
        canvas.create(8, 4)
        command = Command(Command.Keyword.RECT, 2, 2, 7, 4)
        self.assertEqual(executor.execute(canvas, command), 0)

    def test_execute_rect_wrong_args_num_throws(self):
        executor = Executor()
        canvas = Canvas()
        canvas.create(8, 4)
        command = Command(Command.Keyword.RECT, 1, 4, 10)
        self.assertRaises(ValueError, executor.execute, canvas, command)

    def test_execute_rect_wrong_types_throws(self):
        executor = Executor()
        canvas = Canvas()
        canvas.create(8, 4)
        command = Command(Command.Keyword.RECT, 1, 4, 10, 'str')
        self.assertRaises(TypeError, executor.execute, canvas, command)

    def test_execute_fill_wrong_types_throws(self):
        executor = Executor()
        canvas = Canvas()
        canvas.create(8, 4)
        command = Command(Command.Keyword.FILL, 1, 'str', 'o')
        self.assertRaises(TypeError, executor.execute, canvas, command)


if __name__ == '__main__':
    t = CommandExecutorTest()

