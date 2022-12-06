# Day 6 of the 2022 Advent of Code
# Read input file
with open("../include/input6.inc","r") as data_file:
    data_str = data_file.read().strip()

marker_buffer = []
char_count = 0
start_done = False
for character in data_str:
    char_count+=1
    # If character exists in buffer, it now starts after the existing character
    if character in marker_buffer:
        i = marker_buffer.index(character)
        marker_buffer = marker_buffer[i+1:]
    marker_buffer.append(character)
    # First time it's 4 characters long
    if len(marker_buffer)==4 and not start_done:
        start_count = char_count
        start_done = True
    # First time it's 14 characters long
    elif len(marker_buffer)==14:
        message_count = char_count
        break

print("Part1: %s"%start_count)
print("Part2: %s"%message_count)