for _ in range(int(input())):
    m, s = map(int, input().split())
    b = list(map(int, input().split()))
    b.sort()
    max_value = b[-1]
    first_sum = (max_value*(max_value+1))//2
    sum_b = sum(b)
    if sum_b + s == first_sum:
        print('YES')
    elif sum_b + s < first_sum:
        print('NO')
    else:
        ex = (sum_b+s) - first_sum
        i = max_value + 1
        ans = 0
        while ex > 0:
            ex = ex - i
            i += 1
            if ex == 0:
                ans = 1
        if ans == 1:
            print('YES')
        else:
            print('NO')