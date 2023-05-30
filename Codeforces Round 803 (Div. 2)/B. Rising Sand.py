t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for j in range(1, n-1):
        if a[j] > (a[j-1] + a[j+1]):
            ans += 1
    if k == 1:
        print((n-1)//2)
    else:
        print(ans)

