#!/usr/bin/env python3

from os import path

def main():

    data = get_input()
    rope_partI = [(0,0), (0,0)]
    rope_partII = [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]

    print(f'Part I positions visited: {move_rope(data, rope_partI)}')
    print(f'Part II positions visited: {move_rope(data, rope_partII)}')

def move_rope(data, rope):

    visited = {0: {0}}
    pos_H = rope[0]

    for motion in data:
        for step in range(int(motion.split()[1])):
            # move head
            pos_H = rope[0]
            if motion.split()[0] == 'R':
                pos_H = (pos_H[0] + 1, pos_H[1])
            elif motion.split()[0] == 'L':
                pos_H = (pos_H[0] - 1, pos_H[1])
            elif motion.split()[0] == 'U':
                pos_H = (pos_H[0], pos_H[1] + 1)
            elif motion.split()[0] == 'D':
                pos_H = (pos_H[0], pos_H[1] - 1)
            rope[0] = pos_H

            # move rest of rope
            for knot in range(1, len(rope)):
                rope[knot] = move_tail(rope[knot-1], rope[knot])

            # visited by tail
            if rope[len(rope)-1][0] in visited:
                visited[rope[len(rope)-1][0]].add(rope[len(rope)-1][1])
            else:
                visited[rope[len(rope)-1][0]] = {rope[len(rope)-1][1]}

    positions_visited = 0
    for key in visited:
        positions_visited += len(visited[key])
    return positions_visited


def move_tail(pos_H, pos_T):
    if abs(pos_H[0]-pos_T[0]) <= 1 and abs(pos_H[1]-pos_T[1]) <= 1: # touching
        return pos_T
    elif pos_H[0] == pos_T[0]: # same vertical line
        return (pos_T[0], int((pos_T[1] + pos_H[1]) / 2))
    elif pos_H[1] == pos_T[1]: # same horizontal line
        return (int((pos_T[0] + pos_H[0]) / 2), pos_T[1])
    elif abs(pos_H[0]-pos_T[0]) <= 2 and abs(pos_H[1]-pos_T[1]) <= 1: # diagonal
        return (int((pos_T[0] + pos_H[0]) / 2), pos_T[1] + (pos_H[1] - pos_T[1]))
    elif abs(pos_H[0]-pos_T[0]) <= 1 and abs(pos_H[1]-pos_T[1]) <= 2: # diagonal
        return (pos_T[0] + (pos_H[0] - pos_T[0]), int((pos_T[1] + pos_H[1]) / 2))
    elif abs(pos_H[0]-pos_T[0]) <= 2 and abs(pos_H[1]-pos_T[1]) <= 2: # diagonal
        return (int((pos_T[0] + pos_H[0]) / 2), int((pos_T[1] + pos_H[1]) / 2))

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
