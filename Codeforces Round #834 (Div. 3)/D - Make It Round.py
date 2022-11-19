import math

for t in range(int(input())):
    n, m = map(int, input().split())
    f = 0
    ans = -1
    for j in range(18, 0, -1):
        x = 10 ** j
        g = math.gcd(n, x)
        x = x // g
        if x <= m:
            ans = x
            break
    if ans == -1:
        print(n * m)
        continue
    k = m // ans

    print(ans * n * k)