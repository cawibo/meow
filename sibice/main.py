#Input: The first line of input contains an integer N (1 \leq N \leq 50), the number of matches on the floor, and two integers W and H, the dimensions of the box (1 \leq W \leq 100, 1 \leq H \leq 100).Each of the following N lines contains a single integer between 1 and 1\, 000 (inclusive), the length of one match.

#Output: For each match, in the order they were given in the input, output on a separate line “DA” if the match fits in the box or “NE” if it does not.

import sys, math

n, w, h = [int(e) for e in sys.stdin.readline().split()]
d = math.sqrt(h**2 + w**2)

for _ in range(n):
	if int(sys.stdin.readline()) <= d:
		print("DA")
	else:
		print("NE")