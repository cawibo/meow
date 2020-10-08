import sys

for k in range(1, int(sys.stdin.readline()) + 1):
	_, n = [int(e) for e in sys.stdin.readline().split()]

	s = n
	for i in range(1, n+1):
		s += i

	print(k, s)