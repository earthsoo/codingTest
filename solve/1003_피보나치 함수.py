import sys
input = sys.stdin.readline

def fibonacci(int n):
  if n==0 : 
    return 0;
  elif n==1 :
    return 1;
  else:
    return fibonacci(n-1) + fibonacci(n-2)
    
t = int(input())
for _ in range(t):
  n = int(input())
  
