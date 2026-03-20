import sys
input = sys.stdin.readline

def fibonacci(int n):
  a = 0
  b = 0
  if n==0 :
    a += 1
    return [a, b];
  elif n==1 :
    b += 1
    return [a, b];
  else:
    return fibonacci(n-1) + fibonacci(n-2)

#입력 받기
t = int(input())
for _ in range(t):
  n = int(input())
  
