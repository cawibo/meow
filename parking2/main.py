import sys

for _ in range(int(sys.stdin.readline())):

	n = int(sys.stdin.readline())

	vals = [int(e) for e in sys.stdin.readline().split()]

	print((max(vals) - min(vals))*2)