# -*- coding:utf-8 -*-
def main():
  pi = 3.141592653589
  r = [float(x) for x in input().split()][0]

  print('{:.6f} {:.6f}'.format(pi * r * r, 2 * pi * r))

if __name__ == '__main__':
  main()
