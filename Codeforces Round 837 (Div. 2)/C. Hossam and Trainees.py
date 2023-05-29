import sys
input = sys.stdin.readline

v = int(10 ** 4.5) + 10
prime = [1] * v
my_prime = []
for c in range(2, v):
    if prime[c]:
        my_prime.append(c)
        for d in range(2 * c, v, c):
            prime[d] = 0


def solve(b):
    s = set()
    for i in b:
        for j in my_prime:
            if i % j == 0:
                if j in s:
                    return "YES"
                s.add(j)
                while i % j == 0:
                    i = i // j
        if i != 1:
            if i in s:
                return "YES"
            s.add(i)
    return "NO"


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a))
"""
### Time Limit ###
import math
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if math.gcd(a[i], a[j]) > 1:
                ans += 1
                print("YES")
                break
        if ans == 1:
            break
    else:
        print("NO")
"""

"""
Time limit
def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p] == True:

            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    li = []
    for p in range(2, n + 1):
        if prime[p]:
            li.append(p)
    return li

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    arr = SieveOfEratosthenes(100000)
    d = {}
    for i in range(n):
        x = a[i]
        p = 0
        while arr[p]*arr[p] <= x:
            if x % arr[p] == 0:
                if arr[p] in d:
                    d[arr[p]] += 1
                else:
                    d[arr[p]] = 1
                while x % arr[p] == 0:
                    x = x // arr[p]
            p += 1
        if x != 1:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
    d_keys = d.keys()
    for i in d_keys:
        if d[i] > 1:
            print("YES")
            break
    else:
        print("NO")

"""