# -*- coding:utf-8 -*-
def main():
  n, m, l = map(int, input().split())
  a = []
  for ai in range(n):
    a.append([int(i) for i in input().split()])
  b = []

  for bi in range(m):
    b.append([int(i) for i in input().split()])

  c = [[0 for j in range(l)] for i in range(n)]

  for i in range(n):
    for j in range(l):
      for k in range(m):
        c[i][j] += a[i][k] * b[k][j]

  for ci in c:
    print(' '.join(map(str, ci)))

if __name__ == '__main__':
  main()
