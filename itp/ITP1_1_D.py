# -*- coding: utf-8 -*-

def main():
  S = int(input())
  h = S // 3600
  r = (S - 3600 * h)
  m = r // 60
  s = r % 60
  print('{}:{}:{}'.format(h,m,s))

if __name__ == '__main__':
  main()
