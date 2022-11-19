# This approach , I convert target list to initial list.
# Then calculate to minimum number of total cyclic shift.

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    l = [] # this list append for result.
    tem = a
    for i in range(n, 0, -1):# initial list value n to 1.
        ind = tem.index(i)

        if tem[-1] == i: # if two value are same then zero shift.
            l.append(0)
            tem = tem[:-1] # because last value are not involb this cyclic shift.

        else:
            l.append(ind+1)
            tem = tem[ind+1:] + tem[:ind+1] # ind+1 time cyclic shift this tem arry.
            tem = tem[:-1] # because last value are not involb this cyclic shift.

    print(*l[::-1]) # reverse ans.