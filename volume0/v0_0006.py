# -*- coding:utf-8 -*-
import sys

def readlines_stdin():
  return sys.stdin.readlines()

def reverse_s(s):
  return ''.join(list(reversed(s)))

def main():
  I = readlines_stdin()
  for i in I:
    ii = reverse_s(i.strip()) 
    print(ii)

if __name__ == '__main__':
  main()
