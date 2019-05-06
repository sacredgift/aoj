# -*- coding:utf-8 -*-
def main():
  i = [int(x) for x in input().split()]
  a, b = i[0], i[1]

  print('{} {} {:.5f}'.format(a // b, a % b, a / b))

if __name__ == '__main__':
  main()
