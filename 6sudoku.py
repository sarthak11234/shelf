

grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def get_candidates(grid, row, col):

    if grid[row][col] != 0:
        return set()

    used = set(grid[row])

    for i in range(9):
        used.add(grid[i][col])

  
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3

    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            used.add(grid[i][j])

    return set(range(1, 10)) - used


def propagate(grid):

    while True:
        changed = False

        for row in range(9):
            for col in range(9):

                if grid[row][col] == 0:

                    candidates = get_candidates(grid, row, col)

                
                    if not candidates:
                        return False

             
                    if len(candidates) == 1:
                        grid[row][col] = candidates.pop()
                        changed = True

        if not changed:
            return True


def select_cell(grid):

    best_cell = None
    best_candidates = None

    for row in range(9):
        for col in range(9):

            if grid[row][col] == 0:

                candidates = get_candidates(grid, row, col)

                if best_candidates is None or len(candidates) < len(best_candidates):
                    best_cell = (row, col)
                    best_candidates = candidates

    return best_cell, best_candidates


def solve(grid):

   
    grid = [row[:] for row in grid]

    if not propagate(grid):
        return None

    cell, candidates = select_cell(grid)

    if cell is None:
        return grid

    row, col = cell


    for value in sorted(candidates):

        new_grid = [r[:] for r in grid]
        new_grid[row][col] = value

        result = solve(new_grid)

        if result is not None:
            return result

    return None



def print_grid(grid):

    for i in range(9):

        if i % 3 == 0 and i != 0:
            print("-" * 21)

        for j in range(9):

            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            print(grid[i][j], end=" ")

        print()


# Main program
print("Initial Sudoku:")
print_grid(grid)

solution = solve(grid)

if solution:
    print("\nSolved Sudoku:")
    print_grid(solution)
else:
    print("\nNo solution exists!")
