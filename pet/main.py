import sys

leader = 0
their_score = -1

for i in range(5):
	curr_score = sum([int(e) for e in sys.stdin.readline().split()])
	
	if curr_score > their_score:
		leader = i+1
		their_score = curr_score

print(leader, their_score)