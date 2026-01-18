temples = int(input())
amount = list(map(int, input().split()))
pos = 0
visited = set()
while 0 <= pos < temples:
  visited.add(pos)
  if amount[pos] % 2 == 0:
    amount[pos] = max(0, amount[pos] - 1)
    pos -= 1
  else:
    amount[pos] = max(0, amount[pos] - 1)
    pos += 1
print(len(visited), sum(amount))
    
