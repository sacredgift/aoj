# -*- coding:utf-8 -*-
import sys

def main():
  def ma(a, b):
    g = a
    l = b
    if a < b:
      g = b
      l = a
    while True:
      r = g % l
      if r == 0:
        break
      g = l
      l = r

    return l

  def mi(a, b):
    ac = 1
    bc = 1

    while True:
      aac = a * ac
      bbc = b * bc

      if aac == bbc:
        break
      elif aac < bbc:
        ac += 1
      else:
        bc += 1

    return aac

  I = sys.stdin.readlines()
  for i in I:
    a, b = map(int, i.split())
    print(ma(a, b), mi(a, b))

if __name__ == '__main__':
  main()
