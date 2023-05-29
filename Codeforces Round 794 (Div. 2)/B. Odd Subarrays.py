t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c = 0
    j = 0
    while j < n-1:
        if a[j] > a[j+1]:
            c += 1
            j += 2
        else:
            j += 1
    print(c)
