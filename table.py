import tkinter as tk

from functions_for_table import list_generate
from cursor import Cursor

D_X_FOR_TEXT = 2


class Table:
    """Table widget for Tkinter module"""

    def __init__(self, canvas: tk.Canvas, rows: int, columns: int, cell_size: tuple, x0: int, y0: int):
        """
        :param canvas: canvas where table is located
        :param rows: number of rows in table
        :param columns: number of columns in table
        :param cell_size: (cell width, cell height)
        :param x0: margin from left window border
        :param y0: margin from top window border
        """
        self.rows = rows
        self.columns = columns
        self.cell_width, self.cell_height = cell_size
        self.left = x0
        self.top = y0

        self.canvas = canvas

        self.def_value = ''
        self.table_list = list_generate(self.rows, self.columns, value=self.def_value)

        self.cursor = Cursor(self.canvas, self.cell_height - self.cell_height // 5,
                             self.left + self.cell_width // 10, self.top + self.cell_height // 10)
        self.cur_pos = [0, 0]

    def draw_table(self):
        """draw the table and text in it on given canvas"""
        self.canvas.delete("table_rect")
        self.canvas.delete("table_text")
        self.move_cursor(self.cur_pos[1], self.cur_pos[0])
        for i in range(self.rows):
            for j in range(self.columns):
                self.canvas.create_rectangle(self.left + self.cell_width * j, self.top + self.cell_height * i,
                                             self.left + self.cell_width * (j + 1),
                                             self.top + self.cell_height * (i + 1),
                                             tags="table_rect")
                self.canvas.create_text(self.left + self.cell_width * j + D_X_FOR_TEXT,
                                        self.top + self.cell_height * (i + 0.5),
                                        text=self.table_list[i][j], font="Calibri 15", anchor="w", tags="table_text")

    def coords(self, new_x: int, new_y: int):
        """change position of the table
        :param new_x: new margin from left window border
        :param new_y: new margin from top window border
        """
        self.left = new_x
        self.top = new_y

    def change_canvas(self, canvas: tk.Canvas):
        """change canvas of the table and return new coordinates (left top corner)"""
        self.canvas = canvas

    def change_cell_size(self, cell_size: tuple):
        """change size of a cell in the table
        :param cell_size: (cell width, cell height)
        """
        self.cell_width, self.cell_height = cell_size

    def change_rows(self, rows: int):
        """change number of rows in the table
        :param rows: new number of rows
        """
        self.rows = rows

    def change_columns(self, columns: int):
        """change number of columns in the table
        :param columns: new number of rows
        """
        self.columns = columns

    def change_value(self, pos: tuple, new_value):
        """
        change value in element
        :param pos: position of element (column, row)
        :param new_value: new value
        :return: None
        """
        self.table_list[pos[1]][pos[0]] += new_value
        self.draw_table()

    def get_value(self, pos: tuple):
        """
        return value of cell
        :param pos: position of element (column, row)
        :return: value of cell
        """
        return self.table_list[pos[1]][pos[0]]

    def get_value_len(self, pos: tuple):
        """
        return length of value in cell
        :param pos: position of element (column, row)
        :return: length of string
        """
        return len(self.table_list[pos[1]][pos[0]]) * 9

    def get_pos(self, coordinates: tuple):
        """
        return position of cell in the table
        :param coordinates: coordinates of element (left, top)
        :return: position of cell (column, row)
        """
        x, y = coordinates
        if self.left < x < self.left + self.cell_width * self.columns and \
                self.top < y < self.top + self.cell_height * self.rows:
            return (x - self.left) // self.cell_width, (y - self.top) // self.cell_height

    def clear(self):
        """clear all in table"""
        self.table_list = list_generate(self.rows, self.columns, value=self.def_value)

    def move_cursor(self, new_row: int, new_col: int):
        """
        move cursor in new cell
        """
        self.cursor.move_cur(new_row, new_col, self.get_value_len((new_col, new_row)),
                             self.cell_width, self.cell_height)


if __name__ == "__main__":
    pass
