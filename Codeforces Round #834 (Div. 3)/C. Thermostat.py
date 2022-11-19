for _ in range(int(input())):
    l, r, x = map(int, input().split())
    a, b = map(int, input().split())
    if a == b:
        print(0)
    elif abs(a-b) >= x:
        print(1)
    elif abs(a-l) < x and abs(r-a) < x or abs(b-l) < x and abs(r-b) < x:
        print(-1)
    else:
        if abs(a-l) < x:
            if abs(r-b) >= x:
                print(2)
            else:
                print(3)
        elif abs(r-a) < x:
            if abs(b-l) >= x:
                print(2)
            else:
                print(3)
        else:
            print(2)