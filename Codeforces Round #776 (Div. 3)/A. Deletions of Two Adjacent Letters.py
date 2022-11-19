for _ in range(int(input())):
    s = input()
    c = input()
    for i in range(len(s)):
        if c == s[i] and i % 2 == 0:
            print('YES')
            break
    else:
        print('NO')
