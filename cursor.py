import tkinter as tk


class Cursor:
    """class for cursor which is used to edit values in table cells"""

    def __init__(self, canvas: tk.Canvas, cur_height: int, left: int, top: int):
        """
        :param canvas: canvas where cursor is located
        :param cur_height: height of vertical (!) cursor
        :param left: margin from left window border
        :param top: margin from top window border
        """
        self.canvas = canvas
        self.height = cur_height
        self.width = 1
        self.left, self.top = left, top

        self.cursor = self.canvas.create_line(self.left, self.top,
                                              self.left, self.top + self.height,
                                              width=self.width, tags="cursor")

    def move_cur(self, row: int, column: int, d_x: int, cell_width: int, cell_height: int):
        """
        change cursor position (move it to specific cell)
        :param cell_height: height of cell in a table
        :param cell_width: height of cell in a table
        :param row: new row
        :param column: new column
        :param d_x: margin which is needed because of numbers in cells
        :return: None
        """
        self.canvas.coords(self.cursor, self.left + column * cell_width + d_x,
                           self.top + row * cell_height, self.left + column * cell_width + d_x,
                           self.top + row * cell_height + self.height)
