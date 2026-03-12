import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  ps = input()
  queue = 0
  
  for s in ps:
    if s == '(':
      queue +=1
    elif s == ')':
      queue -=1
      if queue < 0:
        break
  
  if queue != 0:
    print('NO')
  elif queue == 0:
    print('YES')
