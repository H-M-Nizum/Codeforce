for _ in range(int(input())):
    n = int(input())
    l = [input() for i in range(n)]
    s = set(l)
    ans = ''
    for k in l:
        for i in range(len(k)):
            if k[:i] in s and k[i:] in s:
                if k[:i] in s and k[i:] in s:
                    ans += '1'
                    break
        else:
            ans += '0'
    print(ans)