# -*- coding:utf-8 -*-
def main():
  N = int(input())

  for i in range(N):
    sd = [int(s) for s in input().split()]
    sd.sort()
    sd1, sd2, sd3 = sd[0], sd[1], sd[2]

    r = 'NO'
    if sd3 ** 2 == sd2 ** 2 + sd1 ** 2:
      r = 'YES'
    print(r)

if __name__ == '__main__':
  main()
