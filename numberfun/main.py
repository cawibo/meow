import sys

for _ in range(int(sys.stdin.readline())):

	a, b, c = [int(e) for e in sys.stdin.readline().split()]

	if a+b==c or a-b==c or b-a==c or a*b==c or a/b==c or b/a==c or\
		a+c == b or a-c == b or c-a == b or a*c == b or a/c == b or c/a == b or \
		b+c == a or b-c == a or c-b == a or c*b == a or c/b == a or b/c == a:

		print("Possible")
	else:
		print("Impossible")