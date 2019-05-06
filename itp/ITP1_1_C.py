def main():
  i = input()
  i_array = [int(x) for x in i.split()]
  a, b = i_array[0], i_array[1]

  print(a * b, (a + b) * 2)

if __name__ == '__main__':
  main()
