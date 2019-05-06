# -*- coding:utf-8 -*-
def main():
  for i in range(1, 10001):
    x = input()
    if x == '0':
      break

    print('Case {}: {}'.format(i, x))

if __name__ == '__main__':
  main()
