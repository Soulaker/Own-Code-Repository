import os
import sys

attack = 0
turn = 0
while attack < 2025:
  turn += 1
  if turn % 2 == 0:
    attack += 2
  elif turn % 2 == 1:
    attack += 15
  if turn % 3 == 0:
    attack += 7
  elif turn % 3 == 1:
    attack +=2
  elif turn % 3 == 2:
    attack += 10
  attack +=5
print(turn)

