import sys

flag = False
for s in sys.stdin.readline():
  if s == "s" and flag == True:
    print("hiss")
    sys.exit()
  elif s == "s":
    flag = True
  else:
    flag = False

print("no hiss")