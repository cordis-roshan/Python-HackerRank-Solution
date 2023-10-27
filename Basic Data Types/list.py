x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
z = int(input("Enter the value of z: "))
n = int(input("Enter the value of n: "))
l = []
for i in range(0,x+1):
    for j in range(0, y+1):
        for k in range(0, z+1):
            if i+j+k != n:
                l.append([i,j,k])
print (l)