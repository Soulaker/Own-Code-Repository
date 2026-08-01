ins1 = input()
array1 = [int(a) for a in ins1.split()]
n, q = array1[0], array1[1]
ins2 = input()
goods = [int(b) for b in ins2.split()]
for i in range(2, q + 2):
    ins = input()
    array2 = [int(c) for c in ins.split()]
    op, k, l, r = array2[0], array2[1], array2[2], array2[3]
    p_goods = goods[l - 1:r]
    for j in range(0, len(p_goods)):
        if op == 0:
            if j == 0:
                result = p_goods[0] & k
            else:
                result ^= (p_goods[j] & k)
        if op == 1:
            if j == 0:
                result = p_goods[0] | k
            else:
                result ^= (p_goods[j] | k)
    print(result)

