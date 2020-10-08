#Input: The first line of input contains the integer L (1 \leq L \leq 10\, 000), the number from the task. The second line of input contains the integer D (1 \leq D \leq 10\, 000, L \leq D), the number from the task. The third line of input contains the integer X (1 \leq X \leq 36), the number from the task.

#Output: The first line of output must contain the integer N from the task. The second line of output must contain the integer M from the task.

from sys import stdin

L = int(stdin.readline())
D = int(stdin.readline())
X = int(stdin.readline())

def sum_of_digits(n):
    return sum([int(e) for e in str(n)])

values = [e for e in range(L, D + 1) if sum_of_digits(e) == X]

N = min(values)
M = max(values)

print(N, M, sep="\n")