def calculate_ans(n, a):
    list1 = []
    zero = 0
    for i in range(n - 1, -1, -1):  # count zero
        if a[i] == 0:
            zero += 1
        list1.append(zero)
    l1 = list1[::-1]
    ans = 0
    for i in range(n):
        if a[i] == 1:
            ans += l1[i]
    return ans


for _ in range(int(input())):
    n = int(input())
    lista = list(map(int, input().split()))
    re_a = lista[::-1]
    one = calculate_ans(n, lista)
    try:
        first_zero = lista.index(0)
    except ValueError:
        first_zero = n - 1
    try:
        last_one = re_a.index(1)
        last_one = n - last_one - 1
    except ValueError:
        last_one = 0

    lista[first_zero] = 1
    two = calculate_ans(n, lista)

    lista[first_zero] = 0
    lista[last_one] = 0
    tree = calculate_ans(n, lista)

    print(max(one, two, tree))