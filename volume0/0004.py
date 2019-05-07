# -*- coding:utf-8 -*-
import sys

def main():
  I = sys.stdin.readlines()

  for i in I:
    a, b, c, d, e, f = map(int, i.split())
    y = (-(a * f) + d * c) / (b * d - e * a)
    x  = (c - b * y) / a

    print('{:.3f} {:.3f}'.format(x, y))

if __name__ == '__main__':
  main()
