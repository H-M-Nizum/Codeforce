for i in range(int(input())):
    n, m = map(int, input().split())
    l = []
    for j in range(n):
        s = input()
        l.append(s)
    maxvalue = 1000
    for k in range(n-1):
        for x in range(k+1, n):
            sum = 0
            for y in range(m):
                ans = abs(ord(l[k][y]) - ord(l[x][y]))
                sum += ans
            if sum <= maxvalue:
                maxvalue = sum
    print(maxvalue)