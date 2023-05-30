for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = True
    count = 0
    ind = 0
    for i in range(n):
        count += a[i]
        if count < 0:
            ans = False
            break
        elif count == 0:
            ind = i
            break
    if count != 0:
        print("No")
    else:
        for i in range(ind+1, n):
            if a[i] != 0:
                ans = False
                break
        if ans:
            print("YES")
        else:
            print("NO")
