# Part 1
task = open("task6").read().split("\n\n")

total = [x.replace("\n", "") for x in task]
total = [len(set(x)) for x in total]
print(sum(total))

# Part 2
task = open("task6").read().split("\n\n")
task = [x.split("\n") for x in task]
task = [[set(y) for y in x] for x in task]


def sum_inter(lst):
	return len(lst[0].intersection(*lst))

total = [sum_inter(x) for x in task]
print(sum(total))