import sys

for _ in range(int(sys.stdin.readline())):
  b, p = [float(e) for e in sys.stdin.readline().split()]

  bpm = 60*b / p
  abpm = 60/p

  print(bpm-abpm, bpm, bpm+abpm)