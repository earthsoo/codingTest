import sys
input = sys.stdin.readline
n = int(input())

stack = []
for i in range (n):
  command = list(input().split())
  if command[0] == 'push':
    stack.append(command[1])
    continue
  elif command[0] == 'pop':
    if len(stack) == 0:
      print(-1)
    else:
      p = stack.pop()
      print(p)
    continue
  elif command[0] == 'size':
    print(len(stack))
    continue
  elif command[0] == 'empty':
    if len(stack) == 0:
      print(1)
    else:
      print(0)
    continue
  elif command[0] == 'top':
    if len(stack) == 0:
      print(-1)
      continue
    print(stack[-1])
