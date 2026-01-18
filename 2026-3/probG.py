import math

layers, signs = map(int, input().split())
radius = []
for _ in range(layers):
  radius.append(int(input()))
radius.sort()
ans = 0
for _ in range(signs):
  x, y = map(int, input().split())
  distance = math.hypot(x, y)
  for r in radius:
    if r >= distance:
      ans += 1
print(ans)
    
