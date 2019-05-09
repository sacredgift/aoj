# -*- coding:utf-8 -*-
import sys

def readlines_stdin():
  return list(map(lambda s: s.strip(), sys.stdin.readlines()))

def insert_sort(s):
  A = list(map(int, s.split()))
  for i in range(len(A)):
    v = A[i]
    j = i - 1
    while 0 <= j and v < A[j]:
      A[j + 1] = A[j]
      j -= 1
    A[j + 1] = v
    print(' '.join(map(str, A)))

def main():
  I = readlines_stdin()

  insert_sort(I[1])

if __name__ == '__main__':
  main()
