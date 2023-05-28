for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if k < n:
        ans = 0
        sum_a = 0
        for i in range(n):
            sum_a += a[i]
            if i >= k:
                sum_a -= a[i-k]
            ans = max(ans, sum_a)
        ans += k*(k-1)//2
        print(ans)
    else:
        ans = sum(a) + (n*(n-1)//2) + (n*(k-n))
        print(ans)
