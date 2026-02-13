# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
# BFS 사용

from collections import deque
#수빈:n, 동생: k
n, k = map(int, input().split())

queue = deque()
map = [0] * 100001
queue.append(n)

while queue:
  cur = queue.popleft()
  if cur == k:
    break
  for i in (cur+1, cur-1, 2*cur):
    if 0<= i < 100001 and not map[i]:
      map[i] = map[cur] + 1
      queue.append(i)
print (map[k])
