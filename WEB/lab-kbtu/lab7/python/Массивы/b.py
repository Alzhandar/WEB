n=int(input())
l=[]

for i in range(n):
    k=int(input())
    l.append(k)

for i in range(len(l)):
    if l[i]%2==0:
        print(l[i],end=' ')