#Input: The input is composed of two lines. The first line contains a single positive integer n (1 \le n \le 100) that specifies the number of temperatures collected by the University of Chicago Weather Service. The second line contains n temperatures, each separated by a single space. Each temperature is represented by an integer t (-1\, 000\, 000 \le t \le 1\, 000\, 000)

#Output: You must print a single integer: the number of temperatures strictly less than zero.

import sys

_ = sys.stdin.readline()

numbers = [int(e) for e in sys.stdin.readline().split() if int(e) < 0]

print(len(numbers))
