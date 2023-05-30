t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    n = a+b
    if b>=a:
        for j in range(n):
            if j%2==1 and a>0:
                print('0', end='')
                a -= 1
            else:
                print('1', end='')
    else:
        for j in range(n):
            if j%2==1 and b>0:
                print('1', end='')
                b -= 1
            else:
                print('0', end='')

    print()