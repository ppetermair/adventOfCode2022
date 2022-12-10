#!/usr/bin/env python3

from os import path

def main():

    cycle = 0
    x = 1
    signal_strength = 0
    crt = []
    crt_row = 0
    crt_row_pos = -1
    for i in range(6):
        row = []
        for j in range(40):
            row.append('-')
        crt.append(row)    

    for instruction in get_input():

        value = 0
        duration = 0

        if 'addx' in instruction:
            duration = 2
            value = int(instruction.split(' ')[1])
        else:
            duration = 1
            value = 0
        
        for i in range(duration):
            cycle = cycle + 1
            crt_row_pos = crt_row_pos + 1
            if crt_row_pos == 40:
                crt_row_pos = 0
                crt_row = crt_row + 1

            crt[crt_row][crt_row_pos] = draw_pixel(x, crt_row_pos)
            if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                signal_strength = signal_strength + (cycle * x)

        x = x + value
    
    print(f'Signal strength {signal_strength}')
    print('CRT:')
    for row in crt:
        for pixel in row:
            print(pixel, end= '')
        print()

def draw_pixel(x, pixel):
    sprite_pos_left = x - 1
    sprite_pos_right = x + 1
    if pixel >= sprite_pos_left and pixel <= sprite_pos_right:
        return '#'
    else:
        return '.'

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
