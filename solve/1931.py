import sys
input = sys.stdin.readline

n = int(input())
times = []
for _ in range(n):
  t = tuple(map(int, input().split()))
  times.append(t)

times.sort(key=lambda x: (x[1],x[0])) #종료시간 우선 고려, 같으면 시작시간 고려
cnt = 0
end_time = 0
for time in times:
  if time[0] < end_time:
    continue
  else:
    cnt+=1
    end_time = time[1]
print(cnt)
