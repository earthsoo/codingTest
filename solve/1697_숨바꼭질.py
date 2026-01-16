# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
# BFS 사용

from collections import deque
n, k = map(int, input().split())

queue = deque()
map = [0] * 100001
queue.append(n)
