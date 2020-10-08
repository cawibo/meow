#Input: The first line contains two integers, n, the number of cards, and s, the desired sum. The second line will contain n integers between 1 and 100\, 000\, 000 inclusive. You may assume that 1\leq n\leq 100\, 000 and 2\leq s\leq 200\, 000\, 000.

#Output: The output should be a single line consisting of the string YES if two cards can be chosen such that (in some orientation) they add up to s, and the string NO otherwise.

import sys

unflippable = set(["3", "4", "7"])

flips = {
    "1": "1",
    "2": "2",
    "5": "5",
    "6": "9",
    "8": "8",
    "9": "6",
    "0": "0",
}

def flip(card):
    return "".join([flips[c] for c in reversed(card)])

def flippable(card):
    for c in card:
        if c in unflippable:
            return False
    return True

n, s = [int(e) for e in sys.stdin.readline().split()]
potential = set()

for card in sys.stdin.readline().split():
    value = int(card)

    if (s-value) in potential:
        print("YES")
        break    

    if flippable(card):
        flipped = int(flip(card))
        
        if (s-flipped) in potential:
            print("YES")
            break

        potential.add(flipped)

    potential.add(value)
else:
    print("NO")
