import sys
input = sys.stdin.readline

c = int(input())
for _ in range(c):
  l = list(map(int, input().split()))
  av = (sum(l) - l[0]) % l[0]

