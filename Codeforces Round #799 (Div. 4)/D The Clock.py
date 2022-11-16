for _ in range(int(input())):
    a, b = input().split()
    b = int(b)
    h, m = map(int,a.split(":"))
    t, ans, d, s = h*60+m, 0, set(), 1440
    while not (t in d):
        h, m = t // 60, t % 60
        c = ("0" + str(h))[-2:] + ":" + ("0" + str(m))[-2:]
        if c == c[::-1]:
            ans += 1
        d.add(t)
        t = (t + b) % s
    print(ans)