# -*- coding:utf-8 -*-
def main():
  n = int(input())

  dic = {'S': [i for i in range(1,14)],
         'H': [i for i in range(1,14)],
         'C': [i for i in range(1,14)],
         'D': [i for i in range(1,14)]}

  for c in range(n):
    a = [i for i in input().split()]
    k, n = a[0], int(a[1])

    dic[k].remove(n)

  for k in ['S', 'H', 'C', 'D']:
    for n in dic[k]:
      print(k,n)

if __name__ == '__main__':
  main()
