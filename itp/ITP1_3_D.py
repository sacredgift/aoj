# -*- coding:utf-8 -*-
def main():
  i = input()
  i_array = [int(x) for x in i.split()]
  a, b, c = i_array[0], i_array[1], i_array[2]

  e = b + 1
  r = 0
  for j in range(a, e):
    if c % j == 0:
      r += 1

  print(str(r))

if __name__ == '__main__':
  main()
