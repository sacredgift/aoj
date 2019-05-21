# -*- coding:utf-8 -*-
import sys

def readlines_stdin():
  return list(map(lambda s: s.strip(), sys.stdin.readlines()))

def gcd(i):
  x, y = map(int, i.split())

  tmp = 0
  while x % y != 0:
    tmp = y
    y = x % y
    x = tmp

  print(y)

def main():
  I = readlines_stdin()

  for i in I:
    gcd(i)

if __name__ == '__main__':
  main()
