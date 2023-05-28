for _ in range(int(input())):
    n = int(input())
    d = {}
    for i in range(2*n):
        s = input()
        for j in s:
            if j in d:
                d[j] += 1
            else:
                d[j] = 1
    s = input()
    for j in s:
        if j in d:
            d[j] += 1
        else:
            d[j] = 1
    # This char has number of odd time in all strings, this is initial string.
    value_d = d.keys()
    for i in value_d:
        if d[i] % 2 == 1:
            print(i)
            break
