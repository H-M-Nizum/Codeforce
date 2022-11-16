for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for j in range(n):
        b, c = input().split()

        for k in range(int(b)):
            if c[k] == 'D':
                a[j] += 1
                if a[j] == 10:
                    a[j] = 0
            elif c[k] == 'U':
                a[j] -= 1
                if a[j] == -1:
                    a[j] = 9
    print(*a)