ins1 = input()
array1 = [int(i) for i in ins1.split()]
n, w = array1[0], array1[1]
ins2 = input()
array2 = [int(j) for j in ins2.split()]
consumes = 0
for x in range(0, len(array2)):
  consumes += array2[x]
  if consumes > w:
    print(x)
    break
  elif x == len(array2) - 1:
    print(n)
    break

