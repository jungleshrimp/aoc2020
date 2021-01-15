# Part 1

import numpy as np

A = np.loadtxt(fname="task1")

from itertools import combinations
from math import prod


def rSubset(arr, r):
	return list(combinations(arr, r))


for x in rSubset(A, 2):
	if sum(x) == 2020:
		print(x)
		print(prod(x))


# Part 2

import numpy as np

A = np.loadtxt(fname="task1")

from itertools import combinations
from math import prod


def rSubset(arr, r):
	return list(combinations(arr, r))


for x in rSubset(A, 3):
	if sum(x) == 2020:
		print(x)
		print(prod(x))

