# Day 9 of the 2022 Advent of Code
def part1():
    head_pos = [0,0]
    tail_pos = head_pos.copy()
    tail_travel_list = [tail_pos]
    for line in motion_list:
        # Store last tail postion and define next movement
        prev_tail_pos = tail_pos.copy()
        dir = dir_dict[line.split(" ")[0]]
        val = int(line.split(" ")[1])
        
        # Move head according do defined movement
        head_pos = list(map(lambda a,b: val*a+b,dir,head_pos))
        
        # In case tail is more than 1 spot farther, it needs to move closer and register the spots it passed
        if any(x>1 for x in list(map(lambda a,b: abs(a-b),head_pos,tail_pos))):
            tail_pos = list(map(lambda a,b: a-b,head_pos,dir))
            # If x is static it moves in the y axis, otherwise it moves in the x axis
            if dir[0]==0:
                for i in range(prev_tail_pos[1]+dir[1],tail_pos[1],dir[1]): tail_travel_list.append([tail_pos[0],i])
            else:
                for i in range(prev_tail_pos[0]+dir[0],tail_pos[0],dir[0]): tail_travel_list.append([i,tail_pos[1]])
            tail_travel_list.append(tail_pos)
    return tail_travel_list

def sign(num):
    if num>0: return 1
    elif num<0: return -1
    else: return 0

def moveNextKnot(current_knot,knot_list):
    # If any coordinate is more than 1 spot from the previous knot, move it
    if any(x>1 for x in list(map(lambda a,b: abs(a-b),knot_list[current_knot],knot_list[current_knot-1]))):
        aux_knot = knot_list[current_knot].copy()
        for i in range(2): aux_knot[i] += sign(knot_list[current_knot-1][i] - knot_list[current_knot][i])
        knot_list[current_knot] = aux_knot.copy()
        
        # If last knot add this spot to the travel list, otherwise move to next knot
        if current_knot == len(knot_list)-1: tail_travel_list.append(knot_list[current_knot])
        else: knot_list = moveNextKnot(current_knot+1,knot_list)
    return knot_list

def part2(num_knots):
    knot_list = [[0,0]]*num_knots
    for line in motion_list:
        # Move head and next knots accordingly, one step at a time
        for _ in range(int(line.split(" ")[1])):
            knot_list[0] = list(map(lambda a,b: a+b,dir_dict[line.split(" ")[0]],knot_list[0]))
            knot_list = moveNextKnot(1,knot_list)
    return tail_travel_list

# Read input file
with open("../include/input9.inc","r") as motion_file:
    motion_list = list(map(lambda a: a.strip(),motion_file.readlines()))

tail_travel_list = [[0,0]]
dir_dict = {"R":[0,1],
            "L":[0,-1],
            "U":[1,0],
            "D":[-1,0]}

print("Part1: %s"%len(set(tuple(i) for i in part1())))
print("Part2: %s"%len(set(tuple(i) for i in part2(10))))