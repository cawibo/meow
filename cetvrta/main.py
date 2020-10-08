import sys

left = [0] * 1000
right = [0] * 1000

for _ in range(3):
	l, r = [int(e) for e in sys.stdin.readline().split()]
	left[l] += 1
	right[r] += 1

for i in range(1000):
	if left[i] == 1:
		print(i, end=" ")
		break

for i in range(1000):
	if right[i] == 1:
		print(i)
		break
