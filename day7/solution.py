#!/usr/bin/env python3

from os import path

def main():

    filesystem = create_filesystem()
    calculate_sizes(filesystem)
    free = 70_000_000 - filesystem['size']
    need = 30_000_000 - free
    
    print(f'Part I sum of directories {sum_of_directory_sizes(filesystem, 100000)}')
    print(f'Part II size of smallest directory to delete {find_lowest_dir_size(filesystem, need)}')

def find_lowest_dir_size(directory, min_size):
    size = 10**100

    for dir in directory['dir']:
        lowest_size = find_lowest_dir_size(directory['dir'][dir], min_size)
        if lowest_size > min_size and lowest_size < size:
            size = lowest_size
    
    if directory['size'] > min_size and directory['size'] < size:                      
            size = directory['size']

    return size

def sum_of_directory_sizes(directory, max_size):
    size = 0
    for dir in directory['dir']:
        size += sum_of_directory_sizes(directory['dir'][dir], max_size)
    if directory['size'] <= max_size:
        size += directory['size']
    return size

def calculate_sizes(directory):
    size = 0
    for file in directory['file']:
        #print(directory['file'][file])
        size += directory['file'][file]
        #print(size)
    for dir in directory['dir']:
        size += calculate_sizes(directory['dir'][dir])
    directory['size'] = size
    #print(directory)
    return size

def create_filesystem():
    filesystem = create_directory()
    filesystem['dir']['/'] = create_directory()
    path = [filesystem]
    current_directory = filesystem

    for line in get_input():
        if "$ cd" in line:
            directory = line.split(' ')[2]
            if directory in current_directory['dir']:
                path.append(current_directory)
                current_directory  = current_directory['dir'][directory]
            elif ".." == directory:
                current_directory = path.pop()
            else:
                current_directory = current_directory['dir'][directory]
        elif "dir " in line:
            directory = line.split(' ')[1]
            current_directory['dir'][directory] = create_directory()
        elif line[0].isdigit():
            current_directory['file'][line.split(' ')[1]] = int(line.split(' ')[0])
    return filesystem

def create_directory():
    return {
        'dir': {},
        'file': {},
        'size': 0
    }

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
