from itertools import combinations
n, m = input().split()
n = sorted(n)
for k in range(1, int(m)+1):
    x = sorted(list(combinations(n, int(k))))
    x = sorted(x)
    for i in x:
        print("".join(i))