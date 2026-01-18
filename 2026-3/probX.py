import sys

def palin(word, start, end):
  for i in range(end - start):
    if word[start + i] != word[end - i]:
      return False
  return True

word = sys.stdin.read().strip()
ans = 1
for j in range(len(word)):
  for i in range(j + 1, len(word)):
    if palin(word, j, i):
      ans = max(ans, i - j + 1)
print(ans)

