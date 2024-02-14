f_in = open("input1", "r")

pattern = [("zero", "z0o"), ("one", "o1e"), ("two", "t2o"), ("three", "t3e"), ("four", "f4r"),
           ("five", "f5e"), ("six", "s6x"), ("seven", "s7n"), ("eight", "e8t"), ("nine", "n9e")]

num_list_q1 = []
num_list_q2 = []

for line in f_in:
    nums = [c for c in line if c.isdigit()]
    num_list_q1.append(int(str(nums[0]) + str(nums[-1])))
    # replace words by numbers by preserving overlapping structure
    for t in pattern:
        line = line.replace(*t)
    nums = [c for c in line if c.isdigit()]
    num_list_q2.append(int(str(nums[0]) + str(nums[-1])))

print(f"Question 1: the sum is {sum(num_list_q1)}")
print(f"Question 2: the sum is {sum(num_list_q2)}")
