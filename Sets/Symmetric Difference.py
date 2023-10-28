M = input()
M1 = set(input().split())
N = input()
N1 = set(input().split())
for i in sorted(list(map(int, N1.symmetric_difference(M1)))):
    print(i)
