for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mina = min(a)
    total = sum(a)
    print(total - (mina*n))