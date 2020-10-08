import sys
from collections import Counter

counter = Counter(T=1, C=1, G=1) + Counter(sys.stdin.readline().rstrip())

total = 0
for _, c in counter.items():
	total += (c-1)**2

			# least common
print(total + (counter.most_common()[:-2:-1][0][1]-1)*7)