import sys
input = sys.stdin.readline

c = int(input())
for _ in range(c):
  l = list(map(int, input().split()))
  av = sum(l[1:]) / l[0]
  cnt = sum(1 for score in l[1:] if score > av)
  answer = cnt / l[0] * 100
  print(f"{answer:.3f}", '%', sep = '')
