#Input: Input consists of a single integer N (1 \le N \le 100).

#Output: Output the entire wizard’s spell by counting from 1 to N, giving one number and “Abracadabra” per line.

import sys

for i in range(int(sys.stdin.readline())):
	print("{} Abracadabra".format(i+1))