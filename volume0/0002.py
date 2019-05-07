# -*- coding:utf-8 -*-
import sys
import math

def main():
  l = sys.stdin.readlines()

  for i in l:
    a, b = map(int, i.split())
    r = a + b
    print(int(math.log10(r)) + 1)

if __name__ == '__main__':
  main()
