#!/usr/bin/env python3

from os import path

def main():
    
    data = get_input()
    print(f'Part I top crates {part_one(data)}')
    print(f'Part II top crates {part_two(data)}')

def part_one(data):
    stack_dict = create_stack_dict(data)

    # move instructions
    instructions = data[10:]
    for instruction in instructions:
        split_instruction = instruction.split()
        from_stack = stack_dict[int(split_instruction[3])]
        to_stack = stack_dict[int(split_instruction[5])]
        for amount in range(int(split_instruction[1])):
            crate = from_stack.pop(0)
            to_stack.insert(0, crate)

    top_crates = ''
    for stack in stack_dict.values():
        top_crates +=  stack[0]
    
    return top_crates

def part_two(data):
    stack_dict = create_stack_dict(data)

    # move instructions
    instructions = data[10:]
    for instruction in instructions:
        split_instruction = instruction.split()
        from_stack = stack_dict[int(split_instruction[3])]
        to_stack = stack_dict[int(split_instruction[5])]
        amount = int(split_instruction[1])
        to_move_crates = from_stack[:amount]
        stack_dict[int(split_instruction[3])] = from_stack[amount:]
        stack_dict[int(split_instruction[5])] = to_move_crates + to_stack

    top_crates = ''
    for stack in stack_dict.values():
        top_crates +=  stack[0]
    
    return top_crates

def create_stack_dict(data):
    # parse crate data
    crate_data = data[:8]
    layers = [[line[(x * 4) + 1] for x in range(9)] for line in crate_data]
    stack_dict = {}
    for i in range(9):
        stack_dict[i + 1] = []
    for layer in layers:
        for iditem, item in enumerate(layer):
            if item != ' ':
                stack_dict[iditem + 1].append(item)
    return stack_dict

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i for i in f.readlines()]

if __name__ == '__main__':
    main()
