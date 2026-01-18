import sys

lines = sys.stdin.read().split("\n")
temple, portal = map(int, lines[0].strip().split())
graph = {}
for p in range(portal):
  a, b = map(int, lines[p + 1].strip().split())
  graph.setdefault(a, set()).add(b)
  graph.setdefault(b, set()).add(a)

all_nodes = set()
ans = 0
for start in graph.keys():
  if start in all_nodes:
    continue
  visited = set()
  queue = [start]
  while queue:
    src = queue.pop()
    visited.add(src)
    all_nodes.add(src)
    for dst in graph[src]:
      if dst not in visited:
        queue.append(dst)
  ans += 1
print(ans - 1 + (temple - len(all_nodes)))
            
