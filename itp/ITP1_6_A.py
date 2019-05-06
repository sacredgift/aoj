# -*- coding:utf-8 -*-
def main():
  n = int(input())
  a = [i for i in input().split()]

  r = ' '.join(reversed(a))
  print(r)

if __name__ == '__main__':
  main()
