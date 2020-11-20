"""
Unit tests for canvas module
"""

import unittest
import numpy as np

from canvas import MemoryLessCanvas as Canvas


class CanvasTest(unittest.TestCase):
    def test_create_ok(self):
        canvas = Canvas()
        canvas.create(20, 10)
        self.assertEqual(canvas.width, 20)
        self.assertEqual(canvas.height, 10)

    def test_drawline_horizontal_ok(self):
        canvas = Canvas()
        canvas.create(8, 4)
        canvas.draw_line(2, 2, 6, 2)
        expected = np.asarray([
            [ 32,  32,  32,  32,  32,  32,  32,  32],
            [ 32, 120, 120, 120, 120, 120,  32,  32],
            [ 32,  32,  32,  32,  32,  32,  32,  32],
            [ 32,  32,  32,  32,  32,  32,  32,  32]
        ], dtype='uint8')
        self.assertTrue((canvas.data == expected).all())

    def test_drawline_vertical_ok(self):
        canvas = Canvas()
        canvas.create(8, 4)
        canvas.draw_line(5, 1, 5, 3)
        expected = np.asarray([
            [ 32,  32,  32,  32, 120,  32,  32,  32],
            [ 32,  32,  32,  32, 120,  32,  32,  32],
            [ 32,  32,  32,  32, 120,  32,  32,  32],
            [ 32,  32,  32,  32,  32,  32,  32,  32]
        ], dtype='uint8')
        self.assertTrue((canvas.data == expected).all())

    def test_drawline_inverted_ok(self):
        canvas = Canvas()
        canvas.create(8, 4)
        canvas.draw_line(5, 1, 5, 3)
        canvas2 = Canvas()
        canvas2.create(8, 4)
        canvas2.draw_line(5, 3, 5, 1)
        self.assertTrue((canvas.data == canvas2.data).all())

    def test_drawline_inclined_throws(self):
        canvas = Canvas()
        canvas.create(8, 4)
        self.assertRaises(ValueError, canvas.draw_line, 1, 2, 6, 4)

    def test_drawline_horizontal_cropped_ok(self):
        canvas = Canvas()
        canvas.create(8, 4)
        canvas.draw_line(-2, 2, 10, 2)
        expected = np.asarray([
            [ 32,  32,  32,  32,  32,  32,  32,  32],
            [120, 120, 120, 120, 120, 120, 120, 120],
            [ 32,  32,  32,  32,  32,  32,  32,  32],
            [ 32,  32,  32,  32,  32,  32,  32,  32]
        ], dtype='uint8')
        self.assertTrue((canvas.data == expected).all())

    def test_drawline_vertical_cropped_ok(self):
        canvas = Canvas()
        canvas.create(8, 4)
        canvas.draw_line(5, -3, 5, 14)
        expected = np.asarray([
            [ 32,  32,  32,  32, 120,  32,  32,  32],
            [ 32,  32,  32,  32, 120,  32,  32,  32],
            [ 32,  32,  32,  32, 120,  32,  32,  32],
            [ 32,  32,  32,  32, 120,  32,  32,  32]
        ], dtype='uint8')
        self.assertTrue((canvas.data == expected).all())

    def test_drawrect_ok(self):
        canvas = Canvas()
        canvas.create(8, 5)
        canvas.draw_rect(2, 2, 6, 4)
        expected = np.asarray([
            [ 32,  32,  32,  32,  32,  32,  32,  32],
            [ 32, 120, 120, 120, 120, 120,  32,  32],
            [ 32, 120,  32,  32,  32, 120,  32,  32],
            [ 32, 120, 120, 120, 120, 120,  32,  32],
            [ 32,  32,  32,  32,  32,  32,  32,  32]
        ], dtype='uint8')
        self.assertTrue((canvas.data == expected).all())

    def test_drawrect_no_inner_space_ok(self):
        canvas = Canvas()
        canvas.create(8, 5)
        canvas.draw_rect(2, 2, 6, 3)
        expected = np.asarray([
            [ 32,  32,  32,  32,  32,  32,  32,  32],
            [ 32, 120, 120, 120, 120, 120,  32,  32],
            [ 32, 120, 120, 120, 120, 120,  32,  32],
            [ 32,  32,  32,  32,  32,  32,  32,  32],
            [ 32,  32,  32,  32,  32,  32,  32,  32]
        ], dtype='uint8')
        self.assertTrue((canvas.data == expected).all())

    def test_drawrect_inverted_throws(self):
        canvas = Canvas()
        canvas.create(8, 5)
        self.assertRaises(ValueError, canvas.draw_rect, 6, 4, 1, 2)

    def test_drawrect_cropped_ok(self):
        canvas = Canvas()
        canvas.create(8, 5)
        canvas.draw_rect(-4, -3, 6, 4)
        expected = np.asarray([
            [ 32,  32,  32,  32,  32, 120,  32,  32],
            [ 32,  32,  32,  32,  32, 120,  32,  32],
            [ 32,  32,  32,  32,  32, 120,  32,  32],
            [120, 120, 120, 120, 120, 120,  32,  32],
            [ 32,  32,  32,  32,  32,  32,  32,  32]
        ], dtype='uint8')
        self.assertTrue((canvas.data == expected).all())

    def test_fill_ok(self):
        canvas = Canvas()
        canvas.create(10, 8)
        # Fill all canvas area with 'o' (ord('o') == 111)
        canvas.fill(5, 2, 'o')
        expected = np.asarray([
            [111, 111, 111, 111, 111, 111, 111, 111, 111, 111],
            [111, 111, 111, 111, 111, 111, 111, 111, 111, 111],
            [111, 111, 111, 111, 111, 111, 111, 111, 111, 111],
            [111, 111, 111, 111, 111, 111, 111, 111, 111, 111],
            [111, 111, 111, 111, 111, 111, 111, 111, 111, 111],
            [111, 111, 111, 111, 111, 111, 111, 111, 111, 111],
            [111, 111, 111, 111, 111, 111, 111, 111, 111, 111],
            [111, 111, 111, 111, 111, 111, 111, 111, 111, 111]
        ], dtype='uint8')
        self.assertTrue((canvas.data == expected).all())

        # Attempt to place the base point outside of the canvas - no effect
        canvas.fill(-1, 2, '+')
        self.assertTrue((canvas.data == expected).all())

        # Draw some shapes to complicate the picture
        canvas.draw_line(2, 4, 9, 4)
        canvas.draw_rect(3, 2, 8, 20)
        expected = np.asarray([
            [111, 111, 111, 111, 111, 111, 111, 111, 111, 111],
            [111, 111, 120, 120, 120, 120, 120, 120, 111, 111],
            [111, 111, 120, 111, 111, 111, 111, 120, 111, 111],
            [111, 120, 120, 120, 120, 120, 120, 120, 120, 111],
            [111, 111, 120, 111, 111, 111, 111, 120, 111, 111],
            [111, 111, 120, 111, 111, 111, 111, 120, 111, 111],
            [111, 111, 120, 111, 111, 111, 111, 120, 111, 111],
            [111, 111, 120, 111, 111, 111, 111, 120, 111, 111]
        ], dtype='uint8')
        self.assertTrue((canvas.data == expected).all())

        # Fill regions with various symbols: '+' a.k.a. 43, '*' a.k.a. 42, '.' a.k.a. 46
        canvas.fill(5, 3, '+')
        canvas.fill(6, 7, '*')
        canvas.fill(10, 8, '.')
        expected = np.asarray([
            [ 46,  46,  46,  46,  46,  46,  46,  46,  46,  46],
            [ 46,  46, 120, 120, 120, 120, 120, 120,  46,  46],
            [ 46,  46, 120,  43,  43,  43,  43, 120,  46,  46],
            [ 46, 120, 120, 120, 120, 120, 120, 120, 120,  46],
            [ 46,  46, 120,  42,  42,  42,  42, 120,  46,  46],
            [ 46,  46, 120,  42,  42,  42,  42, 120,  46,  46],
            [ 46,  46, 120,  42,  42,  42,  42, 120,  46,  46],
            [ 46,  46, 120,  42,  42,  42,  42, 120,  46,  46]
        ], dtype='uint8')
        self.assertTrue((canvas.data == expected).all())


if __name__ == '__main__':
    t = CanvasTest()
