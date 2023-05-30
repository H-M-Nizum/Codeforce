for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[-1]+a[-2]+a[-3] not in a:
        print("NO")
    elif a[0]+a[1]+a[2] not in a:
        print("NO")
    elif a[0]+a[1]+a[-1] not in a:
        print("NO")
    elif a[0]+a[-2]+a[-1] not in a:
        print("NO")
    else:
        print("YES")
"""
 summation of 3 positive value always large each 3 value.
 similarly 3 negative value. 
"""