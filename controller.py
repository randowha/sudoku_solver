LAST_POSITIONS = []

def solve_sudoku(sudoku_matrix):
    first_position = find_next_empty_position(sudoku_matrix)
    LAST_POSITIONS.append(first_position)
    return solve_recursively(sudoku_matrix, first_position)

def find_next_empty_position(sudoku_matrix):
    for field_y, sudoku_row in enumerate(sudoku_matrix):
        for field_x, sudoku_field in enumerate(sudoku_row):
            for cell_y, field_row in enumerate(sudoku_field):
                for cell_x, cell in enumerate(field_row):
                    if cell == 0:
                        return (field_y, field_x, cell_y, cell_x)
    # no empty field left
    return None

def solve_recursively(sudoku_matrix, position=(0,0,0,0), number=1):
    # backtracking, no number is possible -> number from last positions needs to be raised by 1
    if number > 9:
        sudoku_matrix[position[0]][position[1]][position[2]][position[3]] = 0
        last_pos = LAST_POSITIONS.pop()
        number = 1 + sudoku_matrix[last_pos[0]][last_pos[1]][last_pos[2]][last_pos[3]]
        solve_recursively(sudoku_matrix, last_pos, number)

    if is_number_allowed(number, sudoku_matrix, position):
        LAST_POSITIONS.append(position)
        sudoku_matrix[position[0]][position[1]][position[2]][position[3]] = number
        next_pos = find_next_empty_position(sudoku_matrix)
        if next_pos is None:
            return sudoku_matrix
        else:
            solve_recursively(sudoku_matrix, next_pos)
    # try next number in same cell
    else:
        solve_recursively(sudoku_matrix, position, number + 1)

def is_number_allowed(number, sudoku_matrix, position):
    field_y, field_x, cell_y, cell_x = position
    if number < 1 or number > 9:
        return False
    # is number already in sudoku 3x3 field?
    if any(number in field for field in sudoku_matrix[field_y][field_x]):
        return False

    # is number already in row?
    row = []
    for x in range(len(sudoku_matrix)):
        row += sudoku_matrix[field_y][x][cell_y]
    if number in row:
        return False

    # is number already in column?
    column = []
    for outer_y in range(len(sudoku_matrix)):
        for y in range(len(sudoku_matrix)):
            column.append(sudoku_matrix[outer_y][field_x][y][cell_x])
    if number in column:
        return False

    return True
