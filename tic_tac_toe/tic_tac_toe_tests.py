from tic_tac_toe import check_grid

# no winner
game = [[1,1,0], [2,2,0], [1,2,0]]
assert check_grid(game) == 0

# row
game = [[1,1,1],[2,2,0],[0,0,0]]
assert check_grid(game) == 1

game = [[1,0,1],[2,2,2],[0,0,0]]
assert check_grid(game) == 2

# ---
# cols
game = [[1,2,0], [1,2,0], [1,0,0]]
assert check_grid(game) == 1

game = [[1,2,0], [1,2,0], [0,2,0]]
assert check_grid(game) == 2

# diag
game = [[1,2,0],[2,1,0],[2,1,1]]
assert check_grid(game) == 1

game = [[1,1,2],[0,2,0],[2,0,0]]
assert check_grid(game) == 2