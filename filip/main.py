import sys

this, that = [e[::-1] for e in sys.stdin.readline().split()]

if int(this) > int(that):
  print(this)
else:
  print(that)