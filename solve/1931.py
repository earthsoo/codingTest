import sys
input = sys.stdin.readline

n = int(input())
times = []
for _ in range(n):
  t = tuple(map(int, input().split()))
  times.append(t)

times.sort(key=lambda x:x[1],x[0]) #종료시간 우선 고려, 같으면 시작시간 고려
cnt = 1
start = times[0,0]
finish = times[0,1]
while True:
  
