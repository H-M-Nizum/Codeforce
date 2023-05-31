t = int(input())
for i in range(t):
    s = input()
    s1 = ''
    li = len(s)
    for j in s:
        if j in s1:  # 2.j jodi s1 a thake s1 ar value and ai j ar vale total 2 ta.
            li -= 2  # 3. ai 2 len komai dibo.
            s1 = ''  # 4. last a s1 ke empty kore dibo.
        else:  # 5. abar same process colbe
            s1 += j  # 1. j ke s1 a append korbo.jodi j s1 a age the na thake.
    print(li)  # 6. oboses a oi value gului thakbe jeigulu remove korte hobe.
