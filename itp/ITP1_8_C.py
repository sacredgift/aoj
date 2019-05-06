# -*- coding:utf-8 -*-
import sys

def main():
  ls = sys.stdin.readlines()

  an = ord('a')
  zn = ord('z')

  t = [0 for i in range(an, zn + 1)]
  for l in ls:
    for c in l.lower():
      cn = ord(c)
      if an <= cn and cn <= zn: 
        t[cn - an] += 1

  for idx, tn in enumerate(t):
    print(chr(idx + an), ':', tn)

if __name__ == '__main__':
  main()
