for _ in range(int(input())):
    n = int(input())
    list1 = list(map(int, input().split()))
    min_a = min(list1)
    ind_min = list1.index(min_a)
    f = list1[:ind_min]
    l = list1[ind_min:]
    if f == sorted(f)[::-1] and l == sorted(l):
        print('YES')
    else:
        print('NO')