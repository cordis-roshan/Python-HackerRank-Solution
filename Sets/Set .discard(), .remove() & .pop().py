n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    x = input().split()
    if x[0] == 'pop':
        s.pop()
    elif x[1] == 'remove':
        s.remove(x[1])
    elif x[1] == 'discard':
        s.discard(x[1])
print(sum(s) )