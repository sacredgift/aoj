# -*- coding:utf-8 -*-
def main():
  for c in range(3000):
    i = input()
    if i == '0 0':
      break

    i_array = [int(x) for x in i.split()]
    x, y = i_array[0], i_array[1]

    txt = i
    if x > y:
      txt = '{} {}'.format(y, x)

    print(txt)

if __name__ == '__main__':
  main()
