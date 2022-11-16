for i in range(int(input())):
    list = []
    col = 0
    row = 0
    ans = 0
    emty = input()
    for j in range(1, 9):
        a = input()
        list.append(a.find('#') + 1)
    for k in range(6):
        if list[k] == list[k + 2]:
            col = k + 2
            row = list[k + 1]

    print(col, row)