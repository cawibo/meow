#Input: The first line of input contains a single integer N (1 \leq N \leq 100), which is the number of periods of constant quality of life during the person’s lifetime.The next N lines describe the periods of life. Each of these lines contains two real numbers q (0 < q \leq 1), which is the quality of life in this period, and y (0 < y \leq 100), which is the number of years in this period. All real numbers will be specified to exactly one decimal place.

#Output: Display the QALY accumulated by the person. Your answer will be considered correct if its absolute error does not exceed 10^{-3}.

import sys

n = int(sys.stdin.readline())

res = 0
for _ in range(n):
	q, n = [float(e) for e in sys.stdin.readline().split()]
	res += q*n

print("{:.3f}".format(res))