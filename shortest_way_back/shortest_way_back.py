def shortest_way_back(path):
    y,x = 0,0 # initial coordinate
    for direction in path:
        if direction == 'N':
            y += 1
        elif direction == 'S':
            y -= 1
        elif direction == 'E':
            x += 1
        elif direction == 'W':
            x -= 1
    
    back_path = ''
    if y != 0:
        back_path += (y * 'S' if y > 0 else -y * 'N')
    if x != 0:
        back_path += (x * 'W' if x > 0 else -x * 'E')

    return back_path
        