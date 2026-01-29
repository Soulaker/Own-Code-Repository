import os
import sys

# 请在此输入您的代码
def exchange():
  a = input()
  b = []
  c = ""
  for i in a:
     b.append(i)
  if b[-1] == "0":
     b.pop()
     b.append("1")
  elif b[-1] == "1":
     b.pop()
     b.append("0")
  for j in b:
     c += j
  return c
print(exchange())