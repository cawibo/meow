import sys

cups = [1, 0, 0]

for e in sys.stdin.readline():
	if e == "A":
		cups[0], cups[1] = cups[1], cups[0]
	elif e == "B":
		cups[1], cups[2] = cups[2], cups[1]
	elif e == "C":
		cups[0], cups[2] = cups[2], cups[0]

for i, v in enumerate(cups):
	if v == 1:
		print(i + 1)
		break