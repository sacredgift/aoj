# -*- coding:utf-8 -*-
def main():
  while True:
    i = [int(x) for x in input().split()]
    H, W = i[0], i[1]

    if H == 0 and W == 0:
      break

    t_b = ''.join(['#' for e in range(W)])
    print(t_b)

    m = '#{}#'.format(''.join(['.' for e in range(W - 2)]))
    for h in range(H - 2):
      print(m)

    print(t_b)

    print()

if __name__ == '__main__':
  main()
