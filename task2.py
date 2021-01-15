# Part 1

task = open("task2").read().strip().split("\n")
print(task)

task = [x.replace(":", "").replace("-", " ").split(" ") for x in task]
print(task)

i = 0
test = 0
res = 0

while i < len(task):
	for x in task[i][-1]:
		if x == task[i][2]:
			test += 1
	if int(task[i][0]) <= test <= int(task[i][1]):
		res += 1
	test = 0
	i += 1

print(res)

# Part 2

task = open("task2").read().strip().split("\n")
print(task)

task = [x.replace(":", "").replace("-", " ").split(" ") for x in task]
print(task)

i = 0
test = 0
res = 0

while i < len(task):
	pos1 = int(task[i][0]) - 1
	pos2 = int(task[i][1]) - 1
	key = task[i][2]
	pswrd = task[i][-1]
	print(key, pswrd[pos1], pswrd[pos2])
	if (pswrd[pos1] == key and pswrd[pos2] != key) or (pswrd[pos2] == key and pswrd[pos1] != key):
		res += 1
	i += 1

print(res)