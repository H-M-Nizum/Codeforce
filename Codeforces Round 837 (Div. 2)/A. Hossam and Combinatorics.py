for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    maxim = max(a)
    minum = min(a)
    if maxim == minum:
        print((n-1) * n)
    else:
        c_max = a.count(maxim)
        c_min = a.count(minum)

        print(2 * c_min * c_max)
