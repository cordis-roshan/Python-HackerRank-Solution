n = int(input())
n1 = set(map(int,input().split()))
m = int(input())
m1 = set(map(int,input().split()))
o1 = n1.union(m1)
print(len(o1))