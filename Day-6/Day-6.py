import math
import pandas as pd
# input_file = "day-6/input.txt"
input_file = "day-6/example.txt"

with open(input_file, 'r') as file:
    lines = file.read().splitlines()

def find_spaces_num(string):
    return [int(num) for num in string.split()]

def find_spaces_op(string):
    return [num for num in string.split()]

# Convert all but the last line to numbers
num_rows = [find_spaces_num(line) for line in lines[:-1]]

# Last line is the operation row
operation = find_spaces_op(lines[-1])

row_lengths = [len(r) for r in num_rows] + [len(operation)]
assert len(set(row_lengths)) == 1

kinda_sum = list(zip(*num_rows, operation))

def puzzle_1(kinda_sum):
    count = 0
    for calc in kinda_sum:
        op_index = len(calc)-1
        op = calc[op_index]
        if op == '+':
            answer = sum(calc[:op_index])
            count += answer
        if op == '*':
            answer = math.prod(calc[:op_index])
            count += answer
    return count
        
print(f'Answer to puzzle 1: {puzzle_1(kinda_sum)}')
