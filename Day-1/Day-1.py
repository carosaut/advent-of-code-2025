
#Puzzle One
start = 50

zero_count = 0

def rotate(starting_point, instruction):
    global zero_count
    
    direction = instruction[0]
    distance = int(instruction[1:])

    if direction == 'R':
        next_point = (starting_point + distance) % 100
        if next_point == 0:
            zero_count += 1

    if direction == 'L':
        next_point = (starting_point - distance) % 100
        if next_point == 0:
            zero_count += 1
    
    return next_point
        
    
with open("Day-1/puzzle_input_1.txt", "r") as f:
    lines = f.read().splitlines()

for instruction in lines:
    start = rotate(start, instruction)

print(zero_count)

