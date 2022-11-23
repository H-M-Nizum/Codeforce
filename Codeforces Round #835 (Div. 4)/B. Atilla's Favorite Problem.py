for _ in range(int(input())):
    n = int(input())
    string = input()
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    ans = 0
    for i in string:
        ind = alfabet.index(i)
        if ans < ind:
            ans = ind
    print(ans+1)