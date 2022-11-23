for _ in range(int(input())):
    x, y, z = map(int, input().split())
    list = [x, y, z]
    list.sort()
    print(list[1])