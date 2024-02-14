import re

f_in = open("input2", "r")

r_cubes = 12
g_cubes = 13
b_cubes = 14

ngames = pgames = 0

for gid, line in enumerate(f_in):
    # set cube counters and game boolean value
    mred_cubes = mgreen_cubes = mblue_cubes = 0
    ggame = True

    # remove game Number and endofline char
    line = line.split(":")[1].replace("\n", "")

    # get max value of each color cube per game
    mred_cubes = max([int(n) for n in re.findall(r'(\d+) red', line)])
    mblue_cubes = max([int(n) for n in re.findall(r'(\d+) blue', line)])
    mgreen_cubes = max([int(n) for n in re.findall(r'(\d+) green', line)])

    ggame = (mred_cubes <= r_cubes and mblue_cubes <= b_cubes and mgreen_cubes <= g_cubes)
    ngames += gid + 1 if ggame else 0

    pgames += mred_cubes * mblue_cubes * mgreen_cubes

print(f"Question 1: the number of possible games = {ngames}")
print(f"Question 2: the sum of the minimum set of cubes power = {pgames}")
