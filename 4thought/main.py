from sys import stdin
from itertools import product

stdin.readline()
for line in stdin.readlines():
	val = int(line)

	solution = None
	for perm in product(["+", "-", "//", "*"], repeat=3):
		string = "4 {} 4 {} 4 {} 4".format(*perm)
		# print(string, " = ", eval(string))
		if val == int(eval(string)):
			solution = "{} = {}".format(string, val)
			break

	if solution:
		print(solution.replace("//", "/"))
	else:
		print("no solution")
		