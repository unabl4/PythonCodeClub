def moveTower(n, src, dst, aux, steps=[]):
    if n > 0:
        # move n-1 disks from the starting pole to the middle pole via the ending pole
        moveTower(n-1, src, aux, dst, steps)
        # move the the most bottom disk from the starting pole to the ending pole
        steps.append([src, dst])
        # move the previously moved n-1 disks from the middle pole to the destination pole
        # with help of the starting pole
        moveTower(n-1, aux, dst, src, steps)
    
    return steps

# main
def hanoi(n):
    ops = moveTower(n, 'starting pole', 'ending pole', 'middle pole', [])
    steps = ["{}. Move disk from {} to {}.".format(y+1, x[0], x[1]) for y,x in enumerate(ops)]
    return '\n'.join(steps)