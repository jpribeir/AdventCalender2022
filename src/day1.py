# Day 1 of the 2022 Advent of Code
# Read input file
with open("../include/input1.inc","r") as calories_file:
    calories_list = list(map(lambda a: a.strip(),calories_file.readlines()))

# Go through calories list
max_cal = 0
total_cal = 0
elf_list = []
for cal in calories_list:
    # If ended the elf calories, update calories list
    if not cal:
        if total_cal > max_cal: max_cal = total_cal
        elf_list.append(total_cal)
        total_cal = 0
    # Else add up his total calories
    else:
        total_cal += int(cal)

# Add up the top 3 elfs
elf_list.sort()
top3 = sum(elf_list[-3:])

print("Part1: %s"%max_cal)
print("Part2: %s"%top3)