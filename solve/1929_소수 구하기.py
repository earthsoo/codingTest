#제곱근 까지만 확인
import math
m, n = map(int, input().split())

for j in range(m, n+1):
  if j < 2:
    continue

  is_prime = True
  for i in range(2, int(math.sqrt(j)) + 1):
    if j % i == 0:
      is_prime = False
      break
  if is_prime == True:
    print(j)

"""
시간 초과 코드
m, n = map(int, input().split())

for j in range (m, n+1):
  for i in range (2, n+1):
    if j == i:
      print (j)
      break
    elif j % i == 0:
      break
"""
