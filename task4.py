# Part 1

task = open("task4").read().split("\n\n")
task = [x.replace("\n", " ").split(" ") for x in task]
# print(task)

test = 0
res = 0

to_check = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

for x in task:
	print(x)
	for y in x:
		print(y)
		for i in to_check[:-1]:
			if y[0:3] == i:
				test += 1
				print(test)
	if test == len(to_check[:-1]):
		res += 1
		test = 0
	test = 0

print(res)

# Part 2
task = open("task4").read().split("\n\n")
task = [x.replace("\n", " ").split(" ") for x in task]
print(task)

test = 0
res = 0

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.

for x in task:
	print(x)
	for y in x:
		print(y)
		if y[0:3] == "byr":
			if 2002 >= float(y[4:]) >= 1920:
				test += 1
		if y[0:3] == "iyr":
			if 2020 >= float(y[4:]) >= 2010:
				test += 1
		if y[0:3] == "eyr":
			if 2030 >= float(y[4:]) >= 2020:
				test += 1
		if y[0:3] == "hgt":
			if y[-2:] == 'in':
				if 76 >= float(y[4:-2]) >= 59:
					test += 1
			if y[-2:] == 'cm':
				if 193 >= float(y[4:-2]) >= 150:
					test += 1
		if y[0:3] == "hcl":
			if len(y) == 11:
				if y[4] == "#":
					if all(c in "0123456789abcedf" for c in y[6:]):
						test += 1
		if y[0:3] == "ecl":
			if y[4:] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
				test += 1
		if y[0:3] == "pid":
			if len(y[4:]) == 9:
				test += 1
		print(test)
	if test == 7:
		res += 1
	test = 0

print(res)

