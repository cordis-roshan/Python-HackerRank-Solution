from itertools import permutations
n, m = input().split()
x = list(permutations(n, int(m)))
x = sorted(x)
for i in x:
    print("".join(i))
