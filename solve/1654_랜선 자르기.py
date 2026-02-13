#영식 k개 보유 중(길이가 모두 다름)
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
links = []
for _ in range(k):
  links.append(int(input()))

lo = 1
hi = max(links)
best = 0
while(lo <= hi):
  mid = (lo + hi) // 2
  s = sum(link // mid for link in links)
  if s < n:
    hi = mid - 1
  else:
    lo = mid + 1
    best = mid

print (best)
