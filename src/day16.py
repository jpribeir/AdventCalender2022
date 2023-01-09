# Day 16 of the 2022 Advent of Code
import re
class Valve():
    def __init__(self,name,rate,neighbours):
        self.name = name
        self.rate = int(rate)
        if neighbours.split(", "): self.neighbours_list = neighbours.split(", ")
        else: self.neighbours_list = [neighbours]

def visitValve(name,time_left,pressure_released,open_list):
    pressure_list = []
    for x in valve_dict[name].neighbours_list: pressure_list.append(visitValve(x,time_left-1,pressure_released,open_list))
    if valve_dict[name].rate > 0 and name not in open_list: 
        aux_open_list = (open_list.copy()).append(name)
        for x in valve_dict[name].neighbours_list: pressure_list.append(visitValve(x,time_left-2,pressure_released,aux_open_list))
    return min(pressure_list)


# Read input file
#with open("../include/input16.inc","r") as valve_file:
with open("../include/example16.inc","r") as valve_file:
    cave_list = list(map(lambda a: a.strip(),valve_file.readlines()))

valve_dict = {}
useful_list = []
for valve in cave_list:
    m = re.match('^Valve (.*) has flow rate=(.*); tunnels? leads? to valves? (.*)$',valve)
    valve_dict[m.group(1)] = Valve(m.group(1),m.group(2),m.group(3))
    if int(m.group(2)): useful_list.append(m.group(1))
    #print(valve_list[-1].name)
    #print(valve_list[-1].rate)
    #print(valve_list[-1].neighbours_list)
    #print("\n")

max_pressure = visitValve("AA",30,0,[])


#print("Part1: %s"%fillCave())