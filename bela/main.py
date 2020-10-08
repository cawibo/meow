import sys

scores = { # [dominant, non-dominant]
	"A": [11, 11],
	"K": [4, 4],
	"Q": [3, 3],
	"J": [20, 2],
	"T": [10, 10],
	"9": [14, 0],
	"8": [0, 0],
	"7": [0, 0]
}

n, b = sys.stdin.readline().split()


score = 0
for _ in range(4*int(n)):
	line = sys.stdin.readline()

	if line[1] == b:
		score += scores[line[0]][0]
	else:
		score += scores[line[0]][1]

print(score)