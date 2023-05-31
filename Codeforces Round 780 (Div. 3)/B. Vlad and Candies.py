t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        if a[0] == 1:
            print("YES")
        else:
            print("NO")
    else:
        arr = sorted(a)
        if (arr[-1] - arr[-2]) <= 1:
            print("YES")
        else:
            print("NO")
