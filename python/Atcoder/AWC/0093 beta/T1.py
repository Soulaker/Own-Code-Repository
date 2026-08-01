ins1 = input()
list1 = [int(i) for i in ins1.split()]
n,m = list1[0],list1[1]
list2 = [0]*n
result = 0
ins2 = input()
list3 = [int(j) for j in ins2.split()]
for l in range(0,m):
  list2[l] = list3[l]
  ins = input()
  list4 = [int(x) for x in ins.split()]
  if list4[l] != 0:
    result += list2[l]
  print(result)
