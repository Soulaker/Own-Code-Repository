'''
ins1 = input()
ins2 = input()
nk = ins1.split()
k = int(nk[1])
array1 = [int(i)for i in ins2.split()]
max1 = max(array1)
array1.remove(max1)
max2 = max(array1)
result = 0
result += (k//2)*(max1+max2)+max1*(k%2)
print(result)
'''
import math
ins1 = input()
array1 = [int(i) for i in ins1.split()]
n, x, y, r = array1[0], array1[1], array1[2], array1[3]
satis = 0
for j in range(0, n):
    flag = 1
    ins = input()
    arrayn = [(l) for l in ins.split()]
    xn, yn, pn = arrayn[0], arrayn[1], arrayn[2]
    distance = math.sqrt((xn - x) ** 2 + (yn - y) ** 2)
    if distance > r:
        flag = 0
    satis += flag * pn
print(satis)
