# -*- coding:utf-8 -*-
def main():
  n = int(input())

  rs = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]

  for c in range(n):
    a = [int(i) for i in input().split()]
    b, f, r, v = a[0] - 1, a[1] - 1, a[2] - 1, a[3]

    t = rs[b][f][r] + v
    rs[b][f][r] = 0 if t < 0 else 9 if 9 < t else t  

  for i, f_a in enumerate(rs):
    for r_a in f_a:
      print(' ' + ' '.join(map(str,r_a)))

    if i < 3:
      print('####################')

if __name__ == '__main__':
  main()
