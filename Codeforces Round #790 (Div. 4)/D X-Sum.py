for _ in range(int(input())):
    n, m = map(int, input().split())
    l = []
    a = [0] * (m + n)
    b = [0] * (m + n)
    ans = 0
    for _ in range(n):
        l.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(m):
            a[i + j] += l[i][j]
            b[i - j] += l[i][j]
    for i in range(n):
        for j in range(m):
            ans = max(ans, a[i + j] + b[i - j] - l[i][j])
    print(ans)