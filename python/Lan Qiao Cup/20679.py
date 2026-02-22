import os
import sys
import string

a = list(string.ascii_lowercase)
b = [int(i) for i in range(0,10)]
out = []
origin = input()
for strings in origin:
  if strings in a:
    out.append('L')
  elif int(strings) in b:
    out.append('Q')
result =  "".join(out)
print(result)