#!/usr/bin/env python3

from os import path

def main():

    datastream = get_input()[0]
    print(f'Part I marker position: {find_marker_position(datastream, 4)}')
    print(f'Part II marker position: {find_marker_position(datastream, 14)}')

def find_marker_position(datastream, distinct_character):
    for i in range(len(datastream)):
        start = i
        end = i + distinct_character
        characters = set(datastream[start:end])
        if len(characters) == distinct_character:
            return end

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
