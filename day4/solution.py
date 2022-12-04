#!/usr/bin/env python3

from os import path

def main():

    partial_overalap = 0
    full_overlap = 0

    for assignment in get_input():
        
        range1 = tuple([int(r) for  r in assignment.split(',')[0].split('-')])
        range2 = tuple([int(r) for  r in assignment.split(',')[1].split('-')])

        # Part I
        if range1[0] <= range2[0] and range1[1] >= range2[1]:
            full_overlap = full_overlap + 1
        elif range2[0] <= range1[0] and range2[1] >= range1[1]:
            full_overlap = full_overlap + 1
        
        # Part II
        if range1[0] <= range2[0] and range1[1] >= range2[0]:
            partial_overalap = partial_overalap + 1
        elif range2[0] <= range1[0] and range2[1] >= range1[0]:
            partial_overalap = partial_overalap + 1
    
    print(f'Pairs with full overlap: {full_overlap}')
    print(f'Pairs with partial overlap: {partial_overalap}')

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
