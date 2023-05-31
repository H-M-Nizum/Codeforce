for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    li, r, answer, x, y = -1, 0, 1, n, 0
    while r <= n:
        while r < n and a[r] != 0:
            r += 1

        result = 1
        for i in range(li + 1, r):
            result *= a[i]
            if result > answer:
                answer, x, y = result, li + 1, n - i - 1

        result = 1
        for i in range(r - 1, li, -1):
            result *= a[i]
            if result > answer:
                answer, x, y = result, i, n - r

        li, r = r, r + 1

    print(x, y)
