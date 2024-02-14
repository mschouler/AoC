import re


f_in = open("input4", "r").read().splitlines()

npoints = 0
sc_num = [1] * (len(f_in))

for lid, line in enumerate(f_in):
    parsed_line = line.split(":")[1].replace("\n", "").split("|")
    w_tick, p_tick = [[int(n) for n in re.findall(r'\d+', str_)] for str_ in parsed_line]
    w_num = [i for i in p_tick if i in w_tick]
    npoints += 2 ** (len(w_num) - 1) if w_num else 0

    for card in range(len(w_num)):
        sc_num[lid + 1 + card] += 1 * sc_num[lid]

print(f"Question 1: the number of points = {npoints}")
print(f"Question 2: the number of scratch cards = {sum(sc_num)}")
