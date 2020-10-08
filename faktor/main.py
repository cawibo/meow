import sys
from math import ceil

articles, impact = [int(e) for e in sys.stdin.readline().split()]

# print("articles {}, impact {}".format(articles, impact))
# print("impact after {}".format(impact-0.99))
print(ceil(articles * (impact-0.99)))