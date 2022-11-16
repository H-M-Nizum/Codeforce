def binary_search(arr, l, r, element):
    l = 0
    r = len(arr) - 1
    ans = 0
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == element:
            return mid + 1
        elif arr[mid] < element:
            l = mid + 1

        else:
            r = mid - 1
            ans = mid
    return ans + 1


for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    sort_a = sorted(a)[::-1]
    for i in range(1, n):
        sort_a[i] += sort_a[i - 1]
    for i in range(q):
        x = int(input())
        if sort_a[-1] < x:
            print(-1)
        else:
            print(binary_search(sort_a, 0, n - 1, x))