import sys

n = int(sys.stdin.readline())
res = 0

for _ in range(n):
    p = sys.stdin.readline().strip()

    number = int(p[:-1])
    pow = int(p[-1])

    res += number**pow

print(res)
