with open("day-5/input.txt", 'r') as file:
    lines = file.read().splitlines()

index = lines.index('')
ids = lines[index+1:]
ranges = lines[:index]

list_of_ranges = []

for i in ranges:
    start, end = map(int, i.split('-'))
    list_of_ranges.append((start,end))

ids_list = list(map(int, ids))

def in_range(id):
    return any(start <= id <= end for start, end in list_of_ranges)

answer = [id for id in ids_list if in_range(id)]

print(f'Puzzle 1 answer: {len(answer)}')

# puzzle 2

new_ranges = []

list_of_ranges.sort(key=lambda x: x[0])

index = 0

while index < len(list_of_ranges):
    try:
        current_start, current_end = list_of_ranges[index]
        max_index = len(list_of_ranges) - 1
        next_index = index

        while next_index < max_index and list_of_ranges[next_index + 1][0] <= current_end:
            next_index += 1
            next_end = list_of_ranges[next_index][1]
            current_end = max(current_end, next_end) 

        new_ranges.append((current_start, current_end))
        index = next_index + 1 

    except IndexError:
        print(index, list_of_ranges[index])
        index += 1

count = sum(r[1] - r[0] + 1 for r in new_ranges)

print(f'Puzzle 2 answer: {count}')



