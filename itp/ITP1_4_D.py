# -*- coding:utf-8 -*-
def main():
  n = int(input())
  a = [int(x) for x in input().split()]

  print(min(a), max(a), sum(a))

if __name__ == '__main__':
  main()
