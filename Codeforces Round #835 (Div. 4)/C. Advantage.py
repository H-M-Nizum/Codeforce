for _ in range(int(input())):
    n = int(input())
    list1 = list(map(int, input().split()))
    sorted_list = sorted(list1)
    first = sorted_list[-1]
    send = sorted_list[-2]
    l = []
    for i in range(n):
        if list1[i] == first:
            l.append(list1[i] - send)
        else:
            l.append(list1[i] - first)
    print(*l)