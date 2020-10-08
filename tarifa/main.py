#Input: The first line of input contains the integer X (1 \leq X \leq 100). The second line of input contains the integer N (1 \leq N \leq 100). Each of the following N lines contains an integer P_ i (0 \leq P_ i \leq 10\, 000), the number of megabytes spent in each of the first N months of using the plan. Numbers P_ i will be such that Pero will never use more megabytes than he actually has.

#Output: The first and only line of output must contain the required value from the task.

import sys

x = int(sys.stdin.readline())
n = int(sys.stdin.readline())

r = 0
for _ in range(n):
	v = int(sys.stdin.readline())
	r += x - v

print(r+x)