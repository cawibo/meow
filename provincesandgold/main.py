import sys

g, s, c = [int(e) for e in sys.stdin.readline().split()]
g *= 3
s *= 2

victory_card = None
if g + s + c >= 8:
	victory_card = "Province"
elif g + s + c >= 5:
	victory_card = "Duchy"
elif g + s + c >= 2:
	victory_card = "Estate"

treasure_card = None
if g + s + c >= 6:
	treasure_card = "Gold"
elif g + s + c >= 3:
	treasure_card = "Silver"
else:
	treasure_card = "Copper"

if victory_card:
	print(victory_card, end=" or ")
print(treasure_card)