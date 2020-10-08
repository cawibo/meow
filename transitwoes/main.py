import sys

s, t, n = [int(e) for e in sys.stdin.readline().split()]
d = [int(e) for e in sys.stdin.readline().split()]
b = [int(e) for e in sys.stdin.readline().split()]
c = [int(e) for e in sys.stdin.readline().split()]

time = 0

time += sum(d) + sum(b)

if time > t - s:
	print("no")

else:
	passed = 0
	for i in range(n):
		passed += d[i] # walking

		while passed % c[i] != 0: # waiting
			passed += 1

		passed += b[i] # bussing

	passed += d[-1]

	if passed > t - s:
		print("no")

	else:
		print("yes")