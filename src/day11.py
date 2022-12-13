# Day 11 of the 2022 Advent of Code
# Class to instantiate directories, detailing its parent directory and child directories/files
class Monkey():
    def __init__(self,num):
        self.num = num
        self.item_list = []
        self.operation = ""
        self.tester = 1
        self.res_true = 0
        self.res_false = 0
    
    def updateItem(self,index):
        operA,operB = self.operation.split(" ")[1],self.operation.split(" ")[2]
        if operB == "old": operB = self.item_list[index]
        if operA == "+": self.item_list[index] += int(operB)
        elif operA == "*": self.item_list[index] *= int(operB)
        self.item_list[index] = int(self.item_list[index]) / 3
    
    def testItem(self,index):
        if self.item_list[index] % self.tester == 0: print("yes")

def noteCheck(line,monkey_list):
    if line.startswith("Monkey"): monkey_list.append(Monkey((line.split(":")[0]).split()[1]))
    elif line.startswith("Starting"): monkey_list[-1].item_list = list(map(int,(line.split(":")[1].replace(" ","")).split(",")))
    elif line.startswith("Operation"): monkey_list[-1].operation = line.split("= ")[1]
    elif line.startswith("Test"): monkey_list[-1].tester = int(line.split("by ")[1])
    elif line.startswith("If true"): monkey_list[-1].res_true = line.split("monkey ")[1]
    elif line.startswith("If false"): monkey_list[-1].res_false = line.split("monkey ")[1]

# Read input file
with open("../include/input11.inc","r") as notes_file:
    notes_list = list(map(lambda a: a.strip(),notes_file.readlines()))

monkey_list = []
throw_dict = {}
for line in notes_list: noteCheck(line,monkey_list)
for i in monkey_list: print(i.item_list)
for monkey in monkey_list: 
    for index,item in enumerate(monkey.item_list):
        monkey.updateItem(index)
        monkey.testItem(index)

#print("Part1: %s"%total_sum)
#print("Part2: %s"%delfolder_size)