import sys

while True:
	n = int(sys.stdin.readline())
	
	if n == -1:
		break

	total = 0
	pre_hours = None
	for _ in range(n):
		miles, hours = [int(e) for e in sys.stdin.readline().split()]

		if pre_hours:
			total += (hours-pre_hours)*miles
		else:
			total += hours*miles

		pre_hours = hours

	print("{} miles".format(total))