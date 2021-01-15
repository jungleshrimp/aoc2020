# Part 1&2

task = open("task5").read().split("\n")
# print(task)


def seat_finder(board_pass):

	row = list(range(128))
	col = list(range(8))

	for y in board_pass[:-3]:
		if y == "F":
			row = row[:len(row) // 2]
		else:
			row = row[len(row) // 2:]

	for y in board_pass[-3:]:
		if y == "L":
			col = col[:len(col) // 2]
		else:
			col = col[len(col) // 2:]
	return row[0] * 8 + col[0]


# Getting all boarding passes
passes = [seat_finder(task[x]) for x in range(len(task))]

# Part 1
print(max(passes))

# Part 2
passes = sorted(passes)

# Getting all seats Ids that should be on the plane
row = list(range(128))
col = list(range(8))
seats = [row[x] * 8 + col[y] for y in col for x in row]
seats = sorted(seats)

# Getting start and end of the list
start = int(passes[0])
end = int(passes[-1])
print(start, end)

# Getting all seats that are on this specific plane
seats = [x for x in seats if start < x < end]

# Result
print(set(seats) - set(passes))