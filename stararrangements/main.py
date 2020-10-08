import sys

n = int(sys.stdin.readline())

print(str(n) + ":")

ans = []

for k in range(1, int(n / 2 + 1)):

	a = n/(2*k + 1)
	if a == int(a):
		# print("{},{}".format(k+1, k))
		ans.append([k+1, k])

	a = (n/k) / 2
	if a == int(a) and k != 1:
		# print("{},{}".format(k, k))
		ans.append([k, k])
	
	a = ((n/k)+1)/2
	if a == int(a) and k != 1:
		# print("{},{}".format(k, k))
		ans.append([k, k])
	
	a = (n+k) / (2*k + 1)
	if a == int(a):
		# print("{},{}".format(k+1, k))
		ans.append([k+1, k])

ans.sort(key=lambda x:x[0])

ans = [str(e[0]) + "," + str(e[1]) for e in ans]

print("\n".join(ans))