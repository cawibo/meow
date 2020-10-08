#Input: The first line contains the three positive integers A, B and C, not necessarily in that order. The three numbers will be less than or equal to 100.The second line contains three uppercase letters ’A’, ’B’ and ’C’ (with no spaces between them) representing the desired order.

#Output: Output A, B and C in the desired order on a single line, separated by single spaces.

import sys

x, y, z = sorted([int(e) for e in sys.stdin.readline().split()])
d = {"A": x, "B": y, "C": z}

res = []
for e in sys.stdin.readline().strip():
    res.append(d[e])

print(" ".join([str(e) for e in res]))
