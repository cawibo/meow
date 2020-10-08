import sys
from math import factorial

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    print(str(factorial(n))[-1])
