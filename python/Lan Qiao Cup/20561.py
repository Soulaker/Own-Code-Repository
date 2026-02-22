import os
import sys
num = 0
for blue in range(0, 256):
  for red in range(0, 256):
    for green in range(0, 256):
        if blue > red and blue > green:
            num += 1
print(num)