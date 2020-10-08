#Input: The first line of input contains the integer x (-1000 \le x \le 1000; x \not= 0). The second line of input contains the integer y (-1000 \le y \le 1000; y \not= 0).

#Output: Output the quadrant number (1, 2, 3 or 4) for the point (x, y).

import sys

x = int(sys.stdin.readline())
y = int(sys.stdin.readline())

if y > 0:
	if x > 0:
		print(1)
	else:
		print(2)
else:
	if x > 0:
		print(4)
	else:
		print(3)
