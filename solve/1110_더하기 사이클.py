n = int(input())
cnt = 0
newnum = 100

fir = n
while (n != newnum):
  #(1)각 자리 숫자 더하기
  sec = (fir // 10) + (fir % 10) 
  #새로운 수 구하기
  newnum = (fir%10)*10 + (sec % 10)
  cnt +=1
  fir = newnum
print(cnt)
