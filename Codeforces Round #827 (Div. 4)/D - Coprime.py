from math import gcd
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    p = -1
    d = {}
    for i in range(n):
        d[l[i]] = i+1
    for i in d:
        for j in d:
            if d[i]+d[j] > p and gcd(i,j) == 1:
                p = d[i]+d[j]
    print(p)