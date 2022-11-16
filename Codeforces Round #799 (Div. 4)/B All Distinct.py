for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = set(a)
    len_a = len(a)
    len_s = len(s)

    if len_a - len_s == 0:
        print(len_a)
    elif (len_a-len_s) % 2 == 0:
        print(len_s)
    else:
        print(len_s-1)