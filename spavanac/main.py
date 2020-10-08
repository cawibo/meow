#Input: The first and only line of input will contain exactly two integers H and M (0 \leq H \leq 23, 0 \leq M \leq 59) separated by a single space, the input time in 24-hour notation. H denotes hours and M minutes.

#Output: The first and only line of output should contain exactly two integers, the time 45 minutes before input time.

import sys

h, m = [int(e) for e in sys.stdin.readline().split()]

if m < 45:
	h = (h-1)%24

m = (m-45)%60

print("{} {}".format(h, m))