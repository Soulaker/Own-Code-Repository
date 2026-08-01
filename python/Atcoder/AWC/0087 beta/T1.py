ins1 = input()
array1 = [int(i)for i in ins1.split()]
t,x,y = array1[0],array1[1],array1[2]
ins2 = input()
ins3 = input()
def move(ways):
  if ways == 'L':
    return -1
  elif ways == 'R':
    return 1
  elif ways == 'S':
    return 0
meet = 0
for j in range(0,t) :
  if x == y :
    meet += 1
    print(j)
  x += move(ins2[j])
  y += move(ins3[j])
print(meet)