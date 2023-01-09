# Day 13 of the 2022 Advent of Code
# Compares int values
def decideVal(left,right):
    if int(left)<int(right): return 1
    elif int(left)>int(right): return 0
    elif int(left)==int(right): return 2

# Triages between ints and lists
def triagePairs(left,right,order):
    if order==1:
        if not isinstance(right,list): right = [right]
    elif order==2: left = [left]
    for i in range(min(len(left),len(right))):
        res = comparePair(left[i],right[i])
        if res==2: pass
        else: return res
    else: return decideVal(len(left),len(right))

# Father function (recursive)
def comparePair(left,right):
    if isinstance(left,list): return triagePairs(left,right,1)
    elif isinstance(right,list): return triagePairs(left,right,2)
    else: return decideVal(left,right)

# Read input file
with open("../include/input13.inc","r") as packet_file:
    packet_list = list(map(lambda a: a.strip(),packet_file.readlines()))

# Group left and right entries in corresponding lists
left_list = []
right_list = []
for i in range(0,len(packet_list),3):
    left_list.append(packet_list[i])
    right_list.append(packet_list[i+1])

# Compare each left/right pair
index_sum = 0
for i in range(len(left_list)): index_sum += (i+1)*comparePair(eval(left_list[i]),eval(right_list[i]))

# Build sorted list with all entries together
complete_list = []
for each in left_list+right_list:
    no_spot = True
    j = 0
    while no_spot:
        if j >= len(complete_list):
            complete_list.append(each)
            no_spot = False
        elif comparePair(eval(each),eval(complete_list[j])):
            complete_list.insert(j,each)
            no_spot = False
        else: j += 1

# Find index for new packets in sorted list
index_prod = 1
for each in ["[[2]]","[[6]]"]:
    for i in range(len(complete_list)):
        if comparePair(eval(each),eval(complete_list[i])):
            complete_list.insert(i,each)
            index_prod *= (i+1)
            break

print("Part1: %s"%index_sum)
print("Part2: %s"%index_prod)