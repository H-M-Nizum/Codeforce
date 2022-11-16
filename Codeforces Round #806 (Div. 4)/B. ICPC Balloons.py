for _ in range(int(input())):
    n = int(input())
    s = input()
    sets = set(s)
    l = len(s) - len(sets)
    print((len(sets)*2) + l)