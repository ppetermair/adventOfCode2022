#!/usr/bin/env python3

from os import path

def main():

    elfs_calorie_count = []
    elf_calorie_count = 0

    for calorie in get_input():
        if calorie:
            elf_calorie_count = elf_calorie_count + int(calorie)
        else:
            elfs_calorie_count.append(elf_calorie_count)            
            elf_calorie_count = 0
    elfs_calorie_count.append(elf_calorie_count) # last one

    elfs_calorie_count.sort()

    print(f'Top 3 calorie counts {elfs_calorie_count[-3:]}')
    print(f'Top calorie count {elfs_calorie_count[-1:][0]}')
    print(f'Top calorie count sum {sum(elfs_calorie_count[-3:])}')

    #print(elfs_calorie_count)

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
