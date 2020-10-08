#Input: The input consist of two lines: One line with the integer N, and one line with N integers k_ i, representing the numbers Robin has written down.

#Output: Output the sum of all the expenses Robin has paid for the last month.

import sys

_ = sys.stdin.readline()

data = [int(e) for e in sys.stdin.readline().split() if int(e) < 0]

res = sum(data)

print(-res)