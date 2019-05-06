# -*- coding:utf-8 -*-
def main():
  while True:
    i = [int(x) for x in input().split()]
    H, W = i[0], i[1]

    if H == 0 and W == 0:
      break

    for h in range(H):
      w = ['#' for e in range(W)]
      print(''.join(w))

    print()

if __name__ == '__main__':
  main()
