
n = 5000
lower = -50000
upper = 50000

f = open("test2.in", "w")
f.write(str(n) + "\n")

import random

l = []
for _ in range(n):
	l.append(str(random.randrange(lower, upper)))

f.write(" ".join(l))