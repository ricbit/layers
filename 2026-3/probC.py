start, end = map(int, input().split())
ans = 0
for i in range(start, 1 + end):
  digits = str(i)
  unique_digits = set(digits)
  if len(digits) == len(unique_digits):
    ans += 1
print(ans)
