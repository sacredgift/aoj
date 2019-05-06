# -*- coding:utf-8 -*-
def main():
  while True:
    i = [int(x) for x in input().split()]
    H, W = i[0], i[1]

    if H == 0 and W == 0:
      break

    odd = ''.join(['.' if e % 2 == 0 else '#' for e in range(W)])
    even = ''.join(['#' if e % 2 == 0 else '.' for e in range(W)])

    for h in range(H):
      result = odd
      if h % 2 == 0:
         result = even
      print(result)

    print()

if __name__ == '__main__':
  main()
