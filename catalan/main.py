import sys
# from math import ceil, factorial
from decimal import Decimal, getcontext
from functools import lru_cache



sys.setrecursionlimit(3000)

getcontext().prec = 3006

n = 5010

def binomial(n, k):
	if n == k or k == 0:
		return 1
	else:
		return binomial(n-1, k-1) + binomial(n-1, k)


def memoize(f):
	
	def helper(n, k):
		if T[n][k] == None:
			T[n][k] = f(n, k)
		return T[n][k]
	return helper

binomial = memoize(binomial)

def catalan(n):
	T = [[None]*n]*n
	this = Decimal(binomial(2*n, n))
	that = (n + 1)
	return this/that

for _ in range(int(sys.stdin.readline())):
	
	print(int(catalan(int(sys.stdin.readline()))))