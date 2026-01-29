a = int(input())
b = input()
d = [int(s) for s in b.split()]
i = 0
for i in range(0,max(d)+1):
  i += 1
  if i not in d:
    print(i)
    break