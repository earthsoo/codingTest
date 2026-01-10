words = input().upper()
dict = {}
for word in words:
  if dict.get(word) == None:
    dict[word] = 1
  else:
    dict[word]+=1
maxValue = 0
maxKey = []
for key, value in dict.items():
  if maxValue < value:
    maxValue = value
    maxKey = [key]
  elif maxValue == value:
    maxKey.append(key)
if len(maxKey) != 1:
  print('?')
else:
  print (*maxKey)
