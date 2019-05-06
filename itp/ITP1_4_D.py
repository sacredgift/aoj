# -*- coding:utf-8 -*-
def main():
  a = [int(x) for x in input().split()]

  print(min(a), max(a), sum(a))

if __name__ == '__main__':
  main()
