#Input: On the first line of the input is a single positive integer T \le 13 the number of test cases to follow. Each case consists of one line containing the integer n (1 \le n \le 13).

#Output: For each test case, output a line with the correct permutation of the values 1 to n, space separated. The first number showing the top card of the pack, etc…

import sys
from collections import deque

# read number of test cases from stdin
T = int(sys.stdin.readline())

# for every testcase
for _ in range(T):
    # read deck size from stdin
    n = int(sys.stdin.readline())

    # create a new deque
    d = deque()

    # for every card in the deck, add the card and then rotate
    for c in reversed(range(1, n+1)):
        d.append(c)
        d.rotate(c+1)
    
    # print result
    print(*d)