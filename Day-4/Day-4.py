with open("Day-4/input-4.txt", "r") as f:
    lines = f.read().splitlines()


start_end_lines = []

for char in range(len(lines[0])):
    start_end_lines.append('x')

# print(start_end_lines)

rows = [start_end_lines]
for line in lines: 
    list_line = list(map(str, line))
    rows.append(list_line)

rows.append(start_end_lines)
# print(rows)
# print(len(rows))

def check_surrounnds(idx, index, row):
    surrounds = []
    prev_row = index-1
    next_row = index+1
    left = idx-1
    right = idx+1
    
    if idx == 0:
        prev_row_left = 'x'
        row_left = 'x'
        next_row_left = 'x'
    
    else:
        prev_row_left = rows[prev_row][left]
        row_left = row[left]
        next_row_left = rows[next_row][left]

    if idx == len(row) - 1:
        prev_row_right = 'x'
        row_right = 'x'
        next_row_right = 'x'

    else:
        prev_row_right = rows[prev_row][right]
        row_right = row[right]
        next_row_right = rows[next_row][right]

    prev_row_above = rows[prev_row][idx]
    next_row_below = rows[next_row][idx]

    surrounds = [prev_row_right, prev_row_above, prev_row_left, row_left, row_right, next_row_left, next_row_below, next_row_right]
    space_count = sum(1 for s in surrounds if s == "@")
    if space_count < 4:  
        return True, idx, index
    else:
        return False, idx, index

# roll_count = 0


def pass_func(rows):
    rolls_to_remove = []
    roll_count = 0
    for index, row in enumerate(rows):
        if index in range(1, len(rows)-1):
            for idx, element in enumerate(row):
                if element == '@':
                    is_space, idx, index = check_surrounnds(idx, index, row)
                    if is_space == True:
                        roll_count += 1
                        rolls_to_remove.append((index, idx))
    for index, idx in rolls_to_remove:
        rows[index][idx] = '.'
    return roll_count

answer_1 = pass_func(rows)
print(f'Puzzle 1 answer: {answer_1}')

total_removed = 0
while True:
    removed = pass_func(rows)   
    if removed == 0:
        break                   
    total_removed += removed

print(f'Puzzle 2 answer: {total_removed + answer_1}')
      
# for row in rows:
#     print(row)  
    



                

