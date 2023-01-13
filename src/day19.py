# Day 19 of the 2022 Advent of Code
import re

# Read input file
#with open("../include/input19.inc","r") as bp_file:
with open("../include/example19.inc","r") as bp_file:
    bp_list = list(map(lambda a: a.strip(),bp_file.readlines()))

max_time = 24
for bp in bp_list:
    m = re.match('^Blueprint (.*)\: Each ore robot costs (.*) ore\. Each clay robot costs (.*) ore\. Each obsidian robot costs (.*) ore and (.*) clay\. Each geode robot costs (.*) ore and (.*) obsidian\.$',bp)
    bp_id = m.group(1)
    orebot_cost = m.group(2)
    claybot_cost = m.group(3)
    obsidianbot_cost = [m.group(4),m.group(5)]
    geodebot_cost = [m.group(6),m.group(7)]

#print("Part1: %s"%fillCave())