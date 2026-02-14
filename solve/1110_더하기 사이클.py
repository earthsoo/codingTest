n = int(input())
cnt = 0
tri = 100 #갱신될 숫자

fir = n
while (n != tri):
  sec = (fir // 10) + (fir % 10)
  tri = (fir%10)*10 + (2nd % 10)
  cnt +=1
print(cnt)
