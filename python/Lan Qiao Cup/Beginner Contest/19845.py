a = int(input())
i = 0
b = []
nums = 0
while i < a:
  c = input()
  b.append(c)
  i += 1
for j in b:
  j = list(j)
  if len(j) == j.count(j[0]):
    nums += 1
print(nums)

