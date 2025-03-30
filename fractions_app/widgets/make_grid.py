from tkinter import ttk


def make_grid(frame: ttk.Frame, rows: int, columns: int) -> None:
    for row in range(rows):
        frame.grid_rowconfigure(row, weight=1)
    for column in range(columns):
        frame.grid_columnconfigure(column, weight=1)
