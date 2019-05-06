# -*- coding:utf-8 -*-
def main():
  i = input()
  i_array = [int(x) for x in i.split()]
  W, H, x, y, r = i_array[0], i_array[1], i_array[2], i_array[3], i_array[4]

  bl = r
  br = W - r
  bt = H - r
  bb = r

  txt = 'No'
  if bl <= x and x <= br and bb <= y and y <= bt:
    txt = 'Yes'
  print(txt)

if __name__ == '__main__':
  main()
