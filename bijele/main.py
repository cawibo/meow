#Input: The input consists of 6 integers on a single line, each between 0 and 10 (inclusive). The numbers are, in order, the numbers of kings, queens, rooks, bishops, knights and pawns in the set Mirko found.

#Output: Output should consist of 6 integers on a single line; the number of pieces of each type Mirko should add or remove. If a number is positive, Mirko needs to add that many pieces. If a number is negative, Mirko needs to remove pieces.

import sys

expected = [1, 1, 2, 2, 2, 8]
current = [int(e) for e in sys.stdin.readline().split()]

res = []
for i, val in enumerate(current):
	this = val
	that = expected[i]

	res.append(that-this)

print(" ".join([str(e) for e in res]))