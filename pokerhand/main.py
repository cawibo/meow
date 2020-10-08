import sys
from collections import Counter

counter = Counter([e[0] for e in sys.stdin.readline().split()])

print(counter.most_common()[0][1])