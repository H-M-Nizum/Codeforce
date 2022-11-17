for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = set(a)
    if len(a) == len(s):
        print('YES')
    else:
        print('NO')