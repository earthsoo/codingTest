#n개의 수가 주어졌을 때 이를 오름차순으로 정렬하는 프로그램
n = int(input())
s = []
for i in range (n):
  s.append(int(input()))
print(set(s.sort()))
