MAZE_MAX_SIZE = 5

# returns the init pos
def find_pos(list):
    pos = [None, None] # positions
    for x in range(MAZE_MAX_SIZE):
        for y in range(MAZE_MAX_SIZE):
            if list[x][y] == 'O': # start
                pos[0] = (x,y)
            elif list[x][y] == 'X': # exit
                pos[1] = (x,y)
    return pos

# given a maze (list) and current position
# returns a list of possible moves (coordinates)
def moves(list, current_pos):
    s = ['.', 'X'] # accepted symbols
    r = range(MAZE_MAX_SIZE) # accepted range
    c = current_pos
    # TODO: change to list comprehension
    m = [(c[0]-1,c[1]), (c[0]+1,c[1]), (c[0],c[1]-1), (c[0], c[1]+1)]
    return filter(lambda c: c[0] in r and c[1] in r and list[c[0]][c[1]] in s, m)

# main
def mazeSolver(list):
    start,end = find_pos(list) # load positions
    distances = { start: 0 }
    visited = set() # O(1) lookup
    queue = [start]

    # bfs
    while queue:
        current_pos = queue.pop(0) # deque (left)
        visited.add(current_pos) # mark as visited

        # are we there yet?
        if current_pos == end:
            return distances[current_pos]

        potential_moves = moves(list,current_pos) # up, down, left, right
        next_moves = filter(lambda m: m not in visited, potential_moves)

        # update distances
        distance = distances.get(current_pos,0) + 1 # increment the distance
        for next_move in next_moves:
            queue.append(next_move)
            distances[next_move] = distance # update

# ---

m = [
    ['*', '*', '*', '*', '*'],
    ['*', '.', '.', '.', '*'],
    ['*', '.', 'O', '.', '*'],
    ['*', 'X', '.', '.', '*'],
    ['*', '*', '*', '*', '*'],
]
assert find_pos(m) == [(2,2),(3,1)]
assert list(moves(m, (1,1))) == [(2,1),(1,2)]
assert mazeSolver(m) == 2

# ---

m = [
    ['O', '.', '.', '.', '.'],
    ['.', '.', '*', '.', '.'],
    ['.', '.', '*', '.', '.'],
    ['.', '.', '*', '*', '*'],
    ['.', '.', '.', '.', 'X'],
]
assert mazeSolver(m) == 8

m = [
    ['O', '.', '.', '.', '.'],
    ['.', '.', '*', '*', '*'],
    ['.', '.', '*', '.', 'X'],
    ['.', '.', '*', '.', '.'],
    ['.', '.', '.', '.', '.'],
]
assert mazeSolver(m) == 10
