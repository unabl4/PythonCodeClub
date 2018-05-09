# checks rows/cols/diags
def check(source):
    for input in source:
        v = set(input) # remove duplicates
        if len(v) == 1:
            n = v.pop()
            if n > 0:
                return n # 1 or 2
    
    return 0

# 0 - draw, 1 - player one, 2 - player two
def check_grid(board):
    n = check(board) # check rows
    if n > 0:
        return n
    
    cols = zip(*board) # transpose
    n = check(cols)
    if n > 0:
        return n

    # diag
    diags = [
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    n = check(diags)
    if n > 0:
        return n

    return 0
