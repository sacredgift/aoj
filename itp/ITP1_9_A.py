# -*- coding:utf-8 -*-
import sys

def main():
  W = input()
  T = sys.stdin.readlines()

  c = 0
  for l in T:
    ll = l.lower().split()
    for w in ll:
      if w == 'end_of_text':
        break
      elif w == W:
        c += 1

  print(c)

if __name__ == '__main__':
  main()
