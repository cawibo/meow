
from sys import stdin

# def mult(a, b):
# 	res = [0] * max(len(a), len(b)) * 2
	
# 	for i_key, i_val in enumerate(a):
# 		for j_key, j_val in enumerate(b):
# 			res[i_key + j_key] += i_val * j_val

# 	return res

from cmath import exp, pi


def fft(a):
	"""
		a: coefficient vector
	"""
	n = len(a)
	if n == 1:
		return a

	even = fft(a[::2])
	odd  = fft(a[1::2])

	# pad such that both part vectors are the same size
	while len(even) < n//2:
		even.append(0)
	while len(odd) < n//2:
		odd.append(0)

	# print("n: ", n)
	# print("len(odd): ", len(odd), ", n//2: ", n//2)

	T = [exp(-2j*pi*k/n)*odd[k] for k in range(n//2)]

	# print("len(even): ", len(even), ", n//2: ", n//2, ", len(T): ", len(T))

	return [even[k] + T[k] for k in range(n//2)] + \
		   [even[k] - T[k] for k in range(n//2)]

def ifft(y):
	"""
		y: point vector
	"""
	n = len(y)
	if n == 1:
		return y

	even = ifft(y[::2])
	odd = ifft(y[1::2])

	while len(even) < n//2:
		even.append(0)
	while len(odd) < n//2:
		odd.append(0)

	T = [1/exp(-2j*pi*k/n)*odd[k] for k in range(n//2)]

	res =  [even[k] + T[k] for k in range(n//2)] + \
		   [even[k] - T[k] for k in range(n//2)]
	
	return res

# https://cp-algorithms.com/algebra/fft.html#toc-tgt-9
# https://ikatanic.github.io/2018/09/22/polynomial-multiplication/
# https://www.geeksforgeeks.org/fast-fourier-transformation-poynomial-multiplication/

def pwmult(A, B):
	return [a*b for a, b in zip(A, B)]


FORCE_POSITIVE = 0

# input
n = int(stdin.readline())
input_values = [int(e) + FORCE_POSITIVE for e in stdin.readline().split()]

freq = [0] * 2*len(input_values)

# make a frequency vector
for val in input_values:
	freq[val + FORCE_POSITIVE] += 1

print("freq: ", freq)

# add len(freq) higher-order zero coefficients
for _ in range(n): freq.append(0)

# get values through fft
values = fft(freq)
print("values: ", values)

# multiply with self
product = pwmult(values, values)

# retrieve coefficient vector
coeff = ifft(product)

print("coeff: ", coeff)

# realize and normalize the values
res = [round(e.real/len(freq)) for e in coeff]

print("res: ", res)

# print("input_values: ", input_values)
for val in input_values:
	res[val*2] -= 1

print("res: ", res)

print("ans: ", sum(res))

ans = sum(res) - 2*1 * 5
print("ans: ", ans)

# for val in values:
	# res[val*2] -= 1

# print("res: ", res)

# ans = 0
# for val in values:
# 	ans += res[val]

# print(ans)



# print(values)

# possible_sums = mult(values, values)
# print(possible_sums)
		#[1, 2, 3] * [2, 4]

