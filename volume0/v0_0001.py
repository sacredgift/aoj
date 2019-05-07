# -*- coding:utf-8 -*-
def main():
  T = [0, 0, 0]
  for i in range(10):
    tt = int(input())
    for ti in range(3):
      if tt > T[ti]:
        ttt = T[ti]
        T[ti] = tt
        tt = ttt

  for ti in T:
    print(str(ti))

if __name__ == '__main__':
  main()
