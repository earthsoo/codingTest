#첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다
"""
dfs : stack, 모든 노드를 방문하고자 하는 경우에 이 방법 선택
bfs : queue, 두 노드 사이의 최단 경로를 찾고 싶을 때
"""
from collections import deque

n, m, v = map(int, input().split())
# 행렬 구성
matrix = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  matrix[a][b] = 1
  matrix[b][a] = 1

def bfs(graph, start):

  queue = deque([start])
  visited[start] = 1
  result = []
  while queue:
    v = queue.popleft()
    result.append(v)
    for neighbor in graph[v]:
      if visited[neighbor] == 0:
        queue.append(neighbor)
        visited[neighbor] = 1
  return result

def dfs(graph, start, visited):
  stack = [start]
  visited[start] = 1
  result = []
  while stack:
    v = stack.pop()
    if visited[v] == 0:
      visited[v] = 1
      result.append(v)
      for neighbor in graph[v]:
        if visited[neighbor] == 0:
          stack.append(neighbor)       
  return result

print(dfs(matrix, v, visited))
print(bfs(matrix, v, visited))
