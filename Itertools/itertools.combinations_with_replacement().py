from itertools import combinations_with_replacement
n, m = input().split()
n = sorted(n)
x =list(combinations_with_replacement(n, int(m)))
for i in x:
    print(''.join(i))
