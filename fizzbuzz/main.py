import sys

x, y, n = [int(e) for e in sys.stdin.readline().split()]

for i in range(1, n+1):
  flag = False
  if i % x == 0:
    flag = True
    print("Fizz", end="")
  if i % y == 0:
    flag = True
    print("Buzz", end="")
  if not flag:
    print(i, end="")

  print()