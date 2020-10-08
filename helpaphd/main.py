#Input: The first line of input will be a single integer N (1 \leq N \leq 1\, 000) denoting the number of testcases. Then follow N lines with either “P=NP” or an addition problem on the form “a+b”, where a, b \in [0, 1\, 000] are integers.

#Output: Output the result of each addition. For lines containing “P=NP”, output “skipped”.

import sys

n = int(sys.stdin.readline())

for _ in range(n):
	data = sys.stdin.readline().strip()
	if data == "P=NP":
		print("skipped")
	else:
		print(eval(data))