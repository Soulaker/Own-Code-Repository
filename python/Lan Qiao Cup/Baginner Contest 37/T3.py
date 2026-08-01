ins = input()
list1 = ins.split()
def fibmod(a,m):
  if a <=2:
    return 1
  else:
    return (fibmod(a-1,m)+fibmod(a-2,m))%m
for i in range(0,10**6):
  if fibmod(i,int(list1[0])) == list1[1]:
    print(i)
    break
