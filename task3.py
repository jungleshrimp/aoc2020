# Part 1
task = open("task3").read().strip().split("\n")
print(task)

# Move is always 3+x and 1+y
x, y = 0, 0
res = 0

for i in range(len(task)):
	if task[y][x] == "#":
		res += 1
	y += 1
	if x < 31-3:
		x += 3
	else:
		x = x+3-31

print(res)

# Part 2
task = open("task3").read().strip().split("\n")
# print(task)


def traverse(x_move, y_move, slope):
	x, y = 0, 0
	res = 0

	for i in range(len(slope)):
		if slope[y][x] == "#":
			res += 1
		if x < 31-x_move:
			x += x_move
		else:
			x = x+x_move-31
		if y <= len(slope) - y_move:
			y += y_move
		else:
			break
	return res


slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

res = [traverse(x[0], x[1], task) for x in slopes]
print(res)

from math import prod
print(prod(res))