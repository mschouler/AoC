import math
from itertools import cycle

f_in = open("input8", "r").read().splitlines()

directions = f_in[0]
coordinates = {ln[0:3]: (ln[7:10], ln[12:15]) for ln in f_in[2:]}
pos_list = [p for p in list(coordinates.keys()) if p[-1] == "A"]
aaa_idx = pos_list.index("AAA")

step_list = [0] * len(pos_list)
for step, dir in enumerate(cycle(list(directions))):
    pos_list = [coordinates[p][0] if dir == "L" else coordinates[p][1] for p in pos_list]
    for idx, p in enumerate(pos_list):
        step_list[idx] = step + 1 if p[-1] == "Z" and step_list[idx] == 0 else step_list[idx]
    if step_list.count(0) == 0:
        break

print(f"Question 1: required number of steps: {step_list[aaa_idx]}")
print(f"Question 2: required number of steps: {math.lcm(*step_list)}")
