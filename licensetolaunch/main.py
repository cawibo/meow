import sys

sys.stdin.readline()

launch_day = 0
launch_junk = 10e9
for i, val in enumerate(sys.stdin.readline().split()):
	val = int(val)
	if val < launch_junk:
		launch_day = i
		launch_junk = val

print(launch_day)