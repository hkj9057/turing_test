a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())
b = [a,b,c,d,e,f,g,h]
a = [1,2,3,4,5,6,7,8]
for i in range(len(b)):

    for j in range(len(b) - 1):

        if(b[j] < b[j+1]):
            b[j],b[j+1] = b[j+1],b[j]
            a[j],a[j+1] = a[j+1],a[j]


plus = 0

for i in range(5):
    plus = b[i] + plus

print(plus)

for i in range(5):

    for j in range(5 - 1):

        if(a[j] > a[j+1]):

            a[j],a[j+1] = a[j+1],a[j]


print("%d %d %d %d %d"%(a[0],a[1],a[2],a[3],a[4]))
