import re


f_in = open("input6", "r").read().splitlines()

time, max_dist = [list(map(int, re.findall(r'\d+', s_line))) for s_line in f_in]
win_num = 1
for r, t in enumerate(time):
    win_num *= len([h_t * (t - h_t) for h_t in range(t) if h_t * (t - h_t) > max_dist[r]])
print(f"Question1: you get {win_num}")

ttime, mmax_dist = [int(re.findall(r'\d+', s_line.replace(" ", ""))[0]) for s_line in f_in]
for h_t in range(ttime):
    if h_t * (ttime - h_t) > mmax_dist:
        break
print(f"Question2: you get {ttime - 2 * h_t + 1}, {h_t}")
