t = int(input())
for j in range(t):
    n = int(input())
    s = input()
    ans = 0
    ans += n
    for i in range(1, n):
        if s[i] != s[i-1]:
            ans += i
    print(ans)