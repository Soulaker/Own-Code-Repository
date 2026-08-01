lines = int(input())
for i in range(0,lines):
    ins = input()
    array1 = [int(j)for j in ins.split()]
    resultmax = 0
    choose = 0
    for x in range(0,3):
        result = array1[x]/array1[x+3]
        if result > resultmax:
            resultmax = result
            choose = x+1
    print(choose)