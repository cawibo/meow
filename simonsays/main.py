import sys

sys.stdin.readline()

for line in sys.stdin.readlines():
	if line[:10] == "Simon says":
		print(line[10:], end="")