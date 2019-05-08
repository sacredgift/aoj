# -*- coding:utf-8 -*-
import sys
import math

max = 1000000
prime_list = [0] * max
count = [0] * max

def readlines_stdin():
  return sys.stdin.readlines()

def is_prime(n):
  if n < 2:
    return False
  if n == 2:
    return True
  if n % 2 == 0:
    return False

  for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
    if n % i == 0:
      return False
  return True

def precount():
  for i in range(1, max):
    if is_prime(i):
      prime_list[i] = 1
      count[i] = count[i - 1] + 1
    else:
      count[i] = count[i - 1]

def main():
  precount()

  I = readlines_stdin()
  for i in I:
    print(count[int(i.strip())])

if __name__ == '__main__':
  main()
