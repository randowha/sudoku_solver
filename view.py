from tkinter import *
from controller import *
from model import *

def create_sudoku():
    root = Tk()
    Sudoku(root)
    root.mainloop()


class Sudoku:
    SIZE = 3
    entries = []

    def __init__(self, root):
        self.create_sudoku_grid_entries(root)
        self.color_entries()

        clearBtn = Button(root, text="Clear", font="Helvetica 15 bold", command=self.clear_sudoku_grid)
        clearBtn.grid(row=Sudoku.SIZE**2, column=Sudoku.SIZE**2 - 2)

        solveBtn = Button(root, text="Solve", font="Helvetica 15 bold", command=self.press_solve, fg="white", bg="black")
        solveBtn.grid(row=Sudoku.SIZE**2, column=Sudoku.SIZE**2 - 1)

    def create_sudoku_grid_entries(self, root):
        validation_callback = root.register(validate_number)

        for outerRow in range(Sudoku.SIZE):
            entries_in_outer_row = []
            for outerColumn in range(Sudoku.SIZE):
                entries_in_outer_column = []
                for innerRow in range(Sudoku.SIZE):
                    entries_in_inner_row = []
                    gridRow = Sudoku.SIZE * outerRow + innerRow
                    for innerColumn in range(Sudoku.SIZE):
                        gridColumn = Sudoku.SIZE * outerColumn + innerColumn
                        entry = Entry(root, width=4, font="Helvetica 20 bold", justify="center", borderwidth=3, validate="key", validatecommand=(validation_callback, "%P"))
                        # entry.insert(END, f'{outerColumn + Sudoku.SIZE*outerRow}{" - "}{innerColumn + Sudoku.SIZE*innerRow}')
                        entry.grid(row=gridRow, column=gridColumn, ipady=15)

                        # build self.entries
                        entries_in_inner_row.append(entry)
                    entries_in_outer_column.append(entries_in_inner_row)
                entries_in_outer_row.append(entries_in_outer_column)
            self.entries.append(entries_in_outer_row)

    def color_entries(self):
        cell_color = ""
        for entries_sudoku_row in Sudoku.entries:
            for entries_sudoku_cell in entries_sudoku_row:
                cell_color = self.switch_color(cell_color)
                for entries_row in entries_sudoku_cell:
                    for entry in entries_row:
                        entry.config({"bg": cell_color, "fg": "black"})
                
                # when Sudoku.SIZE is even (then another color switch necessary at end of row)
                if entries_sudoku_cell == entries_sudoku_row[-1] and Sudoku.SIZE % 2 == 0:
                    cell_color = self.switch_color(cell_color)

    def switch_color(self, lastColor):
        if lastColor == "lightgreen":
            return "lightblue"
        else:
            return "lightgreen"

    def clear_sudoku_grid(self):
        for entries_sudoku_row in Sudoku.entries:
            for entries_sudoku_cell in entries_sudoku_row:
                for entries_row in entries_sudoku_cell:
                    for entry in entries_row:
                        entry.delete(0, 'end')
        self.color_entries()

    def press_solve(self):
        raw_sudoku_entries = Sudoku.entries
        solved_sudoku = solve_sudoku(get_entry_inputs(raw_sudoku_entries))  # controller(model)
        self.show_result(raw_sudoku_entries, solved_sudoku)                 # view

    def show_result(self, raw_sudoku_entries, solved_sudoku):
        self.fill_sudoku(solved_sudoku)
        self.highlight_original_input(raw_sudoku_entries)

    def fill_sudoku(self, solved_sudoku):
        for outerRow in range(Sudoku.SIZE):
            for outerColumn in range(Sudoku.SIZE):
                for innerRow in range(Sudoku.SIZE):
                    for innerColumn in range(Sudoku.SIZE):
                        Sudoku.entries[outerColumn][outerRow][innerColumn][innerRow].insert(END, str(solved_sudoku[outerColumn][outerRow][innerColumn][innerRow]))

    def highlight_original_input(self, raw_sudoku_entries):
        for entries_sudoku_row in raw_sudoku_entries:
            for entries_sudoku_cell in entries_sudoku_row:
                for entries_row in entries_sudoku_cell:
                    for entry in entries_row:
                        if entry.get():
                            entry.config({"bg": "black", "fg": "white"})