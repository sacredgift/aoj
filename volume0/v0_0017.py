# -*- coding:utf-8 -*-
import sys

table = 'abcdefghijklmnopqrstuvwxyz'

def readlines_stdin():
  return list(map(lambda s: s.strip(), sys.stdin.readlines()))

def cipher_tables():
#  that
#  19
#  7
#  0
#  19
#
#  the
#  19
#  7
#  4
#
#  this
#  19
#  7
#  8
#  18
#
  list = []
  for diff in range(26):
    dict = {}
    ci_table = table[-diff:] + table[0:-diff]
    dict['table'] = ci_table
    dict['keywords'] = [
      ''.join([ci_table[19], ci_table[7], ci_table[0], ci_table[19]]),
      ''.join([ci_table[19], ci_table[7], ci_table[4]]),
      ''.join([ci_table[19], ci_table[7], ci_table[8], ci_table[18]])
    ]
    list.append(dict)

  return list

def main():
  I = readlines_stdin()


  for i in I:
    ci_tables = cipher_tables()

    for ci in ci_tables:
      keywords = ci['keywords']
      if keywords[0] in i or keywords[1] in i or keywords[2] in i:
        result = []
        for h in i:
          if h in [' ', '.']:
            r = h
          else:
            r = table[ci['table'].find(h)]
          result.append(r)

        print(''.join(result))

if __name__ == '__main__':
  main()
