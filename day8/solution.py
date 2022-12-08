#!/usr/bin/env python3

from os import path

def main():

    tree_grid = get_tree_grid()
    visible = 0
    max_scenic_score = 0

    for line in range(len(tree_grid)):
        for column in range(len(tree_grid[0])):
            score = get_scenic_score(tree_grid, line, column)
            if score > max_scenic_score:
                max_scenic_score = score
            if is_visible(tree_grid, line, column):
                visible += 1
                
    print(f'Part I visible trees: {visible}')
    print(f'Part II maximum scenic score: {max_scenic_score}')

def get_scenic_score(tree_grid, line, column):
    left_score = column
    right_score = len(tree_grid[0]) - column - 1
    top_score = line
    bottom_score = len(tree_grid) - line - 1

    for i in reversed(range(column)):
        if tree_grid[line][i] >= tree_grid[line][column]:
            left_score = column - i  
            break          
    for i in range(column+1, len(tree_grid[0])):
        if tree_grid[line][i] >= tree_grid[line][column]:
            right_score = i - column
            break
    for i in reversed(range(line)):
        if tree_grid[i][column] >= tree_grid[line][column]:
            top_score = line - i
            break
    for i in range(line+1, len(tree_grid)):
        if tree_grid[i][column] >= tree_grid[line][column]:
            bottom_score = i - line
            break
    return left_score * right_score * top_score * bottom_score

def is_visible(tree_grid, line, column):
    left_visible = True
    right_visible = True
    top_visible = True
    bottom_visible = True
    for i in range(column):
        if tree_grid[line][i] >= tree_grid[line][column]:
            left_visible = False
    for i in range(column+1, len(tree_grid[0])):
        if tree_grid[line][i] >= tree_grid[line][column]:
            right_visible = False
    for i in range(line):
        if tree_grid[i][column] >= tree_grid[line][column]:
            top_visible = False
    for i in range(line+1, len(tree_grid)):
        if tree_grid[i][column] >= tree_grid[line][column]:
            bottom_visible = False
    return left_visible or right_visible or top_visible or bottom_visible

def get_tree_grid():
    tree_grid = []
    for line in get_input():
        line_grid = []
        for tree in line:
            line_grid.append(int(tree))
        tree_grid.append(line_grid)
    return tree_grid

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
