#n개의 수가 주어졌을 때 이를 오름차순으로 정렬하는 프로그램
#시간초과 방지를 위한 readline사용
import sys
input = sys.stdin.readline

n = int(input())
s = []
for i in range(n):
    s.append(int(input()))
s = list(set(s))
s.sort()
print(*s, sep='\n')

"""시간 초과 답안
n = int(input())
s = []
for i in range (n):
  s.append(int(input()))
s = list(set(s))
s.sort()
"""리스트 언패킹(*s) 후 sep으로 enter하"""
print(*s, sep = '\n')
"""
