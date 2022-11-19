for _ in range(int(input())):
    emty = input() #An empty line is written before each test case.
    n, m = map(int, input().split())
    l = []
    for i in range(m):
        x, w = map(int, input().split())
        l.append([w, x, i+1]) # x = coordinate, w = weight and i+1 = index_number/
    l.sort() # sort() for find out smallest weigt value.
    l1 = []
    s = 0
    for i in range(2*n):
        l1.append([l[i][1], l[i][2]]) # l[i][1] = coordinate value, l[i][2] = index value.
        s += l[i][0] # weight value
    print(s)
    l1.sort()
    for i in range(n):
        print(l1[i][1], l1[2*n-i-1][1]) # print first one and last one index number.
    print()