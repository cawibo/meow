import sys

c = float(sys.stdin.readline())
l = int(sys.stdin.readline())

sum = 0
for _ in range(l):
  w1, l1 = [float(e) for e in sys.stdin.readline().split()]
  sum += w1 * l1

print(sum*c)