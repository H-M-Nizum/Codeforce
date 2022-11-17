for _ in range(int(input())):
  a = input() #  is an empty line before each test case.
  y = [input() for i in range(8)]
  print('R' if 8*'R' in y else 'B')