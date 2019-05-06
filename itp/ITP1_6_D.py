# -*- coding:utf-8 -*-
def main():
  n, m = map(int, input().split())

  a = []
  b = []

  for i in range(n):
    a.append([int(j) for j in input().split()])

  for i in range(m):
    b.append(int(input()))

  for ai in a:
    rs = 0
    for aij, bj in zip(ai, b):
      rs += aij * bj
    print(rs)

if __name__ == '__main__':
  main()
