# -*- coding:utf-8 -*-
def main():
  i = input()
  i_array = [int(x) for x in i.split()]
  a, b = i_array[0], i_array[1]

  o = '=='
  if a < b:
    o = '<'
  elif a > b:
    o = '>'
  
  print('a',o,'b')

if __name__ == '__main__':
  main()
