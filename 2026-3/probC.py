start, end = map(int, input().split())
ans = 0
for i in range(start, 1 + end):
  s = str(i)
  t = set(str(i))
  if len(s) == len(t):
    ans += 1
print(ans)
