#!/usr/bin/env python3

from os import path

def main():

    score = {
    'X' : { 'A':1+3, 'B':1+0, 'C':1+6 }, # Rock defeats Scissors
    'Y' : { 'A':2+6, 'B':2+3, 'C':2+0 }, # Paper defeats Rock
    'Z' : { 'A':3+0, 'B':3+6, 'C':3+3 }  # Scissors defeats Paper
    }

    strategy = {
    'X' : { 'A':'Z', 'B':'X', 'C':'Y' }, # lose
    'Y' : { 'A':'X', 'B':'Y', 'C':'Z' }, # draw
    'Z' : { 'A':'Y', 'B':'Z', 'C':'X' }  # win
    }

    part_one_overall_score = 0
    part_two_overall_score = 0

    for round in get_input():
        throw = round.split(' ')
        
        part_one_score = score[throw[1]][throw[0]]
        part_one_overall_score = part_one_overall_score + part_one_score

        part_two_score = score[strategy[throw[1]][throw[0]]][throw[0]]
        part_two_overall_score = part_two_overall_score + part_two_score

    print(f'Part I overall score: {part_one_overall_score}')  
    print(f'Part II overall score: {part_two_overall_score}')  

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
