# Day 11 of the 2022 Advent of Code
# Class to instantiate monkeys
class Monkey():
    def __init__(self,num):
        self.num = num
        self.item_list = []
        self.operation = ""
        self.tester = 1
        self.res_true = 0
        self.res_false = 0
        self.shenanigans_count = 0
    
    # Monkey function goes through whole algorithm
    def throwItems_part1(self):
        throw_list = []
        operA,operB = self.operation.split(" ")[1],self.operation.split(" ")[2]
        for item in self.item_list:
            modified_item = item
            if operB == "old": opermult = modified_item
            else: opermult = operB
            if operA == "+": modified_item += int(opermult)
            elif operA == "*": modified_item *= int(opermult)
            modified_item = int(modified_item/3)
            if modified_item % self.tester == 0: destination_item = (self.res_true,modified_item)
            else: destination_item = (self.res_false,modified_item)
            throw_list.append(destination_item)
            self.shenanigans_count += 1
        self.item_list.clear()
        return throw_list

    # Monkey function goes through whole algorithm
    def throwItems_part2(self):
        operA,operB = self.operation.split(" ")[1],self.operation.split(" ")[2]
        if operB == "old": opermult = self.item_list.copy()
        else: opermult = [int(operB)]*len(self.item_list)
        if operA == "+": out_list = list(map(lambda a,b: a + b,self.item_list,opermult))
        elif operA == "*": out_list = list(map(lambda a,b: a * b,self.item_list,opermult))
        for each in out_list:
            if each % self.tester == 0: monkey_list[self.res_true].item_list.append(each)
            else: monkey_list[self.res_false].item_list.append(each)
        self.shenanigans_count += len(self.item_list)
        self.item_list.clear()

# Reads all notes and builds monkey structure
def noteCheck(line,monkey_list):
    if line.startswith("Monkey"): monkey_list.append(Monkey(int((line.split(":")[0]).split()[1])))
    elif line.startswith("Starting"): monkey_list[-1].item_list = list(map(int,(line.split(":")[1].replace(" ","")).split(",")))
    elif line.startswith("Operation"): monkey_list[-1].operation = line.split("= ")[1]
    elif line.startswith("Test"): monkey_list[-1].tester = int(line.split("by ")[1])
    elif line.startswith("If true"): monkey_list[-1].res_true = int(line.split("monkey ")[1])
    elif line.startswith("If false"): monkey_list[-1].res_false = int(line.split("monkey ")[1])

# Find top 2 busiest monkeys
def findTop2(monkey_list):
    shenanigans_list = []
    for monkey in monkey_list: shenanigans_list.append(monkey.shenanigans_count)
    shenanigans_list.sort()
    return shenanigans_list[-1],shenanigans_list[-2]

# Read input file
with open("../include/example11.inc","r") as notes_file:
#with open("../include/input11.inc","r") as notes_file:
    notes_list = list(map(lambda a: a.strip(),notes_file.readlines()))

monkey_list = []
for line in notes_list: noteCheck(line,monkey_list)
for i in range(20):
    for monkey in monkey_list:
        throw_list = monkey.throwItems_part1()
        for each in throw_list: monkey_list[each[0]].item_list.append(each[1])
        throw_list.clear()
top1,top2 = findTop2(monkey_list)
print("Part1: %s"%(top1*top2))

monkey_list = []
for line in notes_list: noteCheck(line,monkey_list)
for i in range(10000):
    print("### Round %s ###"%i)
    for monkey in monkey_list: monkey.throwItems_part2()
top1,top2 = findTop2(monkey_list)
print("Part2: %s"%(top1*top2))