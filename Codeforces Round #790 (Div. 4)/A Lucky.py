for i in range(int(input())):
    n = input()
    f = 0
    s = 0
    for j in range(3):
        f += int(n[j])
    for k in range(3, 6):
        s += int(n[k])
    if s == f:
        print('YES')
    else:
        print('NO')