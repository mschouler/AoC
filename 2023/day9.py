data = [list(map(int, line.split(" "))) for line in open("input9", "r").read().splitlines()]

num_list = []
for seq in data:
    lst = [seq]
    while lst[-1].count(0) != len(lst[-1]):
        lst.append([lst[-1][i + 1] - lst[-1][i] for i in range(len(lst[-1]) - 1)])

    for idx in range(len(lst) - 1, 0, -1):
        lst[idx - 1].append(lst[idx - 1][-1] + lst[idx][-1])
        lst[idx - 1].insert(0, lst[idx - 1][0] - lst[idx][0])
    num_list.append((lst[0][-1], lst[0][0]))

print(f"question 1: the sum is {sum([t[0] for t in num_list])}")
print(f"question 2: the sum is {sum([t[1] for t in num_list])}")
