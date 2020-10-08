import sys

sys.stdin.readline()

vals = [int(e) for e in sys.stdin.readline().split() if int(e) >= 0]

print(sum(vals) / len(vals))