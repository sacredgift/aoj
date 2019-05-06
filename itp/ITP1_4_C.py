# -*- coding:utf-8 -*-
def main():
  while True: 
    i = [x for x in input().split()]
    if '?' in i:
      break

    a, o, b = int(i[0]), i[1], int(i[2])

    r = 0
    if o == '+':
      r = a + b
    elif o == '-':
      r = a - b
    elif o == '*':
      r = a * b
    elif o == '/':
      r = a // b

    print(r)

if __name__ == '__main__':
  main()
