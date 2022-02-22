import tkinter as tk
from table import Table
from functions_for_program import next_cur_pos, analyze_value, new_value, del_num

ARROWS = ["Up", "Down", "Left", "Right"]

root = tk.Tk()
root.geometry("1000x1000")
root.title("Example window")
canvas = tk.Canvas(root, width=1000, height=1000, bg="white")
canvas.pack()

table = Table(canvas, 13, 13, (70, 40), 12, 15)
table.draw_table()


def move_cur(event):
    if event.keysym in ARROWS:
        next_cur_pos(event.keysym, table)
    else:
        if event.keysym != "BackSpace":
            if analyze_value(event.char, table):
                new_value(event.char, table)
        else:
            del_num(table)


root.bind("<KeyRelease>", move_cur)
root.mainloop()
