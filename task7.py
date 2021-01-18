# Part 1
task = open("task7").read().split("\n")


# Function to find the bags that contain a specific bag
def bagger(bag):
	global task
	bag = [x for x in task if (bag in x) & (bag not in x.split("contain")[0])]
	bag = [x.split("bags")[0] for x in bag]
	return bag


# Recursive function to find all the bags that contain a specific bag
def finding_bags(bags):
	print(bags)

	if len(bags) == 0:
		return

	elif len(bags) == 1:
		res.append(bags[0])
		bags = bagger(bags[0])
		finding_bags(bags)

	else:
		mid = len(bags) // 2
		first_half = bags[:mid]
		second_half = bags[mid:]
		finding_bags(first_half)
		finding_bags(second_half)


res = []
test = bagger("shiny gold")
finding_bags(test)
print(res)
print(len(set(res)))