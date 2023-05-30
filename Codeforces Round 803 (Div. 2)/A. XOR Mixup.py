t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    for j in range(n):
        b = a[j]
        del a[j]
        xora = 0
        for k in range(n-1):
            xora = xora ^ a[k]
        a.insert(i, b)
        if xora == b:
            print(b)
            break
