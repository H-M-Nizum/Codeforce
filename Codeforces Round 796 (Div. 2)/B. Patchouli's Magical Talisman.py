for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    odd = 0
    even = 0
    for i in a:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    # akta odd thaklei, odd+even = odd. so number of even is ans.
    if odd > 0:
        print(even)
    # minimum bar vag kore akta odd ante parle, previous same process.
    else:
        m = a[0]
        for i in a:
            temp = i
            count = 0
            while temp % 2 == 0:
                temp = temp // 2
                count += 1
            m = min(m, count)
        print(m + even - 1)
