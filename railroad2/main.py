import sys

_, y = [int(e) for e in sys.stdin.readline().split()]

if y % 2 == 0:
	print("possible")
else:
	print("impossible")