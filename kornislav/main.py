import sys

vals = sorted([int(e) for e in sys.stdin.readline().split()])

print(vals[0] * vals[-2])

