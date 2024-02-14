import re


def check_line(line: str, lid: int, s: int, n: str, adj_line: bool) -> tuple[str, tuple[int, ...]]:
    a_char = line[s - 1] if s - 1 > 0 else ""
    s_idx = (lid, s - 1) if "*" in a_char else ()

    a_char += line[s + len(n)] if s + len(n) < len(line) else ""
    s_idx = (lid, s + len(n)) if "*" in a_char and not s_idx else s_idx

    if adj_line:
        a_char += line[s: s + len(n)]
        s_idx = (lid, s + line[s: s + len(n)].find("*")) if "*" in a_char and not s_idx else s_idx
    return a_char, s_idx


regex = re.compile("[^a-zA-Z\d\s:.]")
f_l = open("input3", "r").read().splitlines()

part_sum = gear_sum = 0
s_l = []

for lid, line in enumerate(f_l):
    s_n = {m.start(0): m.group(0) for m in re.finditer("\d+", line)}

    for s, n in s_n.items():
        a_char, s_idx = check_line(line, lid, s, n, False)

        if lid > 0:
            tmp_char, tmp_s_idx = check_line(f_l[lid - 1], lid - 1, s, n, True)
            a_char += tmp_char
            s_idx = tmp_s_idx if tmp_s_idx else s_idx

        if lid + 1 < len(f_l):
            tmp_char, tmp_s_idx = check_line(f_l[lid + 1], lid + 1, s, n, True)
            a_char += tmp_char
            s_idx = tmp_s_idx if tmp_s_idx else s_idx

        part_sum += int(n) if regex.search(a_char) is not None else 0

        s_l.append((int(n), s_idx)) if s_idx else ()

gear_sum = sum([t[0] * tt[0] for i, t in enumerate(s_l) for tt in s_l[i + 1:] if t[-1] == tt[-1]])

print(f"Question 1: the sum of all part numbers is {part_sum}")
print(f"Question 2: the sum of all gear ratios is {gear_sum}")
