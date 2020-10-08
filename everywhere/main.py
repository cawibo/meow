import sys

for _ in range(int(sys.stdin.readline())):
    s = set()
    for _ in range(int(sys.stdin.readline())):
      s.add(sys.stdin.readline())

    print(len(s))