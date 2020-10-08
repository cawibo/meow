#Input: The input contains an integer N (1 \leq N \leq 10\, 000\, 000), the number of stones.

#Output: Output the winner, “Alice” or “Bob” (without the quotes), on a line.

import sys

if int(sys.stdin.readline()) % 2 == 0:
	print("Bob")
else:
	print("Alice")