def validate_number(number):
    return (number.isdigit() or number == "") and len(number) <= 1

def get_entry_inputs(raw_sudoku_entries):
    sudoku_matrix = []
    for entries_sudoku_row in raw_sudoku_entries:
        sudoku_outer_row = []
        for entries_sudoku_cell in entries_sudoku_row:
            sudoku_inner_column = []
            for entries_row in entries_sudoku_cell:
                sudoku_inner_row = []
                for entry in entries_row:
                    if entry.get():
                        sudoku_inner_row.append(int(entry.get()))
                    else:
                        sudoku_inner_row.append(0)
                sudoku_inner_column.append(sudoku_inner_row)
            sudoku_outer_row.append(sudoku_inner_column)
        sudoku_matrix.append(sudoku_outer_row)
    
    return sudoku_matrix

