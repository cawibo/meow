import sys
from math import cos, sin, radians

margin = 1
g = 9.81

sys.stdin.readline()

for line in sys.stdin.readlines():
	v0, theta, x1, h1, h2 = [float(e) for e in line.split()]
	theta = radians(theta)

	t_at_wall = (x1 / v0) / cos(theta)
	y_at_wall = (v0 * t_at_wall * sin(theta)) - ((1/2)*g*(t_at_wall**2))

	if y_at_wall >= h1+margin and y_at_wall <= h2-margin:
		print("Safe")
	else:
		print("Not Safe")
