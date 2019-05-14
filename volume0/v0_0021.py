# -*- coding:utf-8 -*-
import sys
from decimal import Decimal

def readlines_stdin():
  return list(map(lambda s: s.strip(), sys.stdin.readlines()))

def is_parallel(x1, y1, x2, y2, x3, y3, x4, y4):
  d1x = x2 - x1
  d1y = y2 - y1
  d2x = x4 - x3
  d2y = y4 - y3

  return d1x * d2y == d1y * d2x

def main():
  I = readlines_stdin()

  for i in range(1, len(I)):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(Decimal, I[i].split())

    rs = 'NO'
    if is_parallel(x1, y1, x2, y2, x3, y3, x4, y4):
      rs = 'YES'
    print(rs)

if __name__ == '__main__':
  main()
