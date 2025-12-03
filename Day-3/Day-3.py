with open("Day-3/Day-3-input.txt", "r") as f:
    lines = f.read().splitlines()

# with open("Day-3/Day-3-examples.txt", "r") as f:
#     lines = f.read().splitlines()

print(lines[0])

# list_of_list_batteries = []
list_of_voltages = []

for line in lines:
    battery = list(map(int, line))
    max_val = max(battery)
    idx_max = battery.index(max_val)
    rest_of_battery = battery[idx_max+1:]
    if not rest_of_battery:
        next_max_val = max_val
        new_bat = battery[:idx_max]
        max_val = max(new_bat)
    else:
        next_max_val = max(rest_of_battery)
    max_val_str = str(max_val) + str(next_max_val)
    max_val_int = int(max_val_str)
    list_of_voltages.append(max_val_int)
    

print(list_of_voltages)
print(f'The answer to part 1 is: {sum(list_of_voltages)}')