for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    if n % 2 == 1:
        print('NO')
    else:
        li = sorted(arr)
        rel = []
        N = n // 2
        for i in range(N):
            rel.append(li[i])
            rel.append(li[N + i])
        rel.append(rel[0])
        rel.append(rel[1])
        ans = 0
        for i in range(1, n + 1):
            if (rel[i] > rel[i - 1] and rel[i] > rel[i + 1]) or (rel[i] < rel[i - 1] and rel[i] < rel[i + 1]):
                continue
            else:
                ans = 1
                break
        if ans == 1:
            print('NO')
        else:
            print('YES')
            print(*rel[:-2])
