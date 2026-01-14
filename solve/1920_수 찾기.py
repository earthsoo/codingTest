import sys
input = sys.stdin.readline

n = int(input())
numsN = set(map(int, input().split()))

m = int(input())
numsM = list(map(int, input().split()))

for num in numsM:
  if num in numsN:
    print(1)
  else:
    print(0)
