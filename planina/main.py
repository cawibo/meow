#Input: The first and only line of input contains one integer N (1 \leq N \leq 15), the number of iterations.

#Output: The first and only line of output should contain one number, the number of points stored after N iterations.

import sys, math 

n = int(sys.stdin.readline())

squares = 4**n
corners = int((math.sqrt(squares) + 1)**2)

print(corners)