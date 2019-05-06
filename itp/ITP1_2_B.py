# -*- coding:utf-8 -*-
def main():
  i = input()
  i_array = [int(x) for x in i.split()]
  a, b, c = i_array[0], i_array[1], i_array[2]

  txt = 'No'
  if a < b and b < c:
    txt = 'Yes'
  print(txt)

if __name__ == '__main__':
  main()
