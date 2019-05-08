# -*- coding:utf-8 -*-
import sys

def readlines_stdin():
  return list(map(lambda s: s.strip(), sys.stdin.readlines()))

def main():
  I = readlines_stdin()

  len_ds = int(I[0])

  for i in range(1, len(I), 2):
    ds_a, ds_b = int(I[i]), int(I[i + 1])
    rs = ds_a + ds_b
    if len(str(rs)) > 80:
      rs = 'overflow'
    else:
      rs = str(rs)
    print(rs)

if __name__ == '__main__':
  main()
