import sys
from math import sin, radians, ceil

h, v = [int(e) for e in sys.stdin.readline().split()]

print(ceil(h / sin(radians(v))))