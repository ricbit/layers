import itertools
import heapq

size = int(input())
startups = []
for _ in range(size):
  days, deadline = map(int, input().split())
  startups.append((deadline, days))
startups.sort(reverse=True)

ans = 0
queue = []
it = itertools.zip_longest(startups, startups[1:], fillvalue=(0, 0))
for cur_startup, next_startup in it:
  t = cur_startup[0] - next_startup[0]
  heapq.heappush(queue, cur_startup[1])
  while t > 0 and queue:
    wiggle = heapq.heappop(queue)
    if wiggle <= t:
      t -= wiggle
      ans += 1
    else:
      heapq.heappush(queue, wiggle - t)
      t = 0
print(ans)

