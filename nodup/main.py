import sys
from collections import Counter

counter = Counter(sys.stdin.readline().split())

print("yes" if counter.most_common()[0][1] == 1 else "no")