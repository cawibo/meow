#Input: The input consists of a single line containing three integers n (2 \leq n \leq 10\, 000), the length of the sides of the square cake in centimeters, h (0 < h < n), the distance of the horizontal cut from the top edge of the cake in centimeters, and v (0 < v < n), the distance of the vertical cut from the left edge of the cake in centimeters. This is illustrated in the figure above.Each cake is 4 centimeters thick.

#Output: Display the volume (in cubic centimeters) of the largest of the four pieces of cake after the horizontal and vertical cuts are made.

import sys

n, h, v = [int(e) for e in sys.stdin.readline().split()]

volume = 4 * max(h, n-h) * max(v, n-v)

print(volume)