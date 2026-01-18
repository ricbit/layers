import sys

word = sys.stdin.read().strip()
current = set()
best = 0
seq = []
for c in word:
  if c in current:
    best = max(best, len(current))
    seq = seq[seq.index(c) + 1:]
    current = set(seq)
  current.add(c)
  seq.append(c)
best = max(best, len(current))
print(best)
