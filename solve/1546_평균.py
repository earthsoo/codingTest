n = int(input())
scores = list((map(int, input().split())))
scoreMax = max(scores)
for i in range(n):
  scores[i] = scores[i]/scoreMax*100
print(sum(scores)/n)
