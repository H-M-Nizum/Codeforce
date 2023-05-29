t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    x = sum(a)
    if x % n == 0:
        if x // n in a:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
