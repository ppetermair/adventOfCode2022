#!/usr/bin/env python3

from os import path

def main():

    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'    
    sum_part_one = 0
    sum_part_two = 0
    group_members = 0
    group_badge = set([c for c in letters])

    for rucksack in get_input():
        
        # Part I
        comp1 = rucksack[0:len(rucksack)//2]
        comp2 = rucksack[len(rucksack)//2:]
        common = set([c for c in comp1]).intersection([c for c in comp2]).pop()
        sum_part_one = sum_part_one + letters.index(common) + 1

        # Part II
        group_members = group_members + 1
        group_badge = group_badge.intersection(set([c for c in rucksack]))
        
        if group_members == 3:
            # add badge priority and reset group variables
            sum_part_two = sum_part_two + letters.index(group_badge.pop()) + 1
            group_members = 0
            group_badge = set([c for c in letters])
       
    print(f'Part I sum: {sum_part_one}')
    print(f'Part II sum: {sum_part_two}')

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
