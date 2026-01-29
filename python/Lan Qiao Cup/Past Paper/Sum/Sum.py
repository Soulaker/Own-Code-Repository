num = int(input())
a = input()
nums = [ int(s) for s in a.split()]
def elv(num,nums):
    i = 0
    j = 1
    sum = 0
    while i< num:
        while j < num:
            sum += nums[i]*nums[j]
            j += 1
        i += 1
        j =i +1
    return sum
print(elv(num,nums))
