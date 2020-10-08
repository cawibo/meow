#Input: The first line contains an integer N (1 \le N \le 100) denoting the number of events. Each of the next N lines contains two integers s_ i and t_ i (1 \le s_ i \le t_ i \le 365) denoting that the i^\textrm {th} event will be held from s_ i to t_ i (inclusive), and free food is served for all of those days.

#Output: The output contains an integer denoting the number of days in which free food is served by at least one event.

import sys

N = int(sys.stdin.readline())

days = set()

for _ in range(N):
	s, t = [int(e) for e in sys.stdin.readline().split()]

	for day in range(s, t+1):
		days.add(day)

print(len(days))