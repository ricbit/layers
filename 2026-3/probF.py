from collections import Counter

def get_sets(counter):
  sets = 0
  for v in counter.values():
    if v < 2:
      return -1
    if v % 3 == 0:
      sets += v // 3
    else:
      sets += v // 3 + 1
  return sets

size = int(input())
music = list(map(int, input().split()))
counter = Counter()
for m in music:
  counter[m] += 1
print(get_sets(counter))
        
        
    
    
