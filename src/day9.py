# Day 9 of the 2022 Advent of Code
# Read input file
with open("../include/input9.inc","r") as motion_file:
    motion_list = list(map(lambda a: a.strip(),motion_file.readlines()))

dir_dict = {"R":[0,1],
            "L":[0,-1],
            "U":[1,0],
            "D":[-1,0]}
head_pos = [0,0]
tail_pos = head_pos.copy()
tail_travel_list = [tail_pos]
for line in motion_list:
    prev_tail_pos = tail_pos.copy()
    dir = dir_dict[line.split(" ")[0]]
    val = int(line.split(" ")[1])
    head_pos = list(map(lambda a,b: val*a+b,dir,head_pos))
    
    # In case tail is more than 1 spot farther, it needs to move closer and register the spots it passed
    if any(x>1 for x in list(map(lambda a,b: abs(a-b),head_pos,tail_pos))):
        tail_pos = list(map(lambda a,b: a-b,head_pos,dir))
        if dir[0]==0:
            for i in range(prev_tail_pos[1]+dir[1],tail_pos[1],dir[1]): tail_travel_list.append([tail_pos[0],i])
        else:
            for i in range(prev_tail_pos[0]+dir[0],tail_pos[0],dir[0]): tail_travel_list.append([i,tail_pos[1]])
        tail_travel_list.append(tail_pos)

print("Part1: %s"%len(set(tuple(i) for i in tail_travel_list)))