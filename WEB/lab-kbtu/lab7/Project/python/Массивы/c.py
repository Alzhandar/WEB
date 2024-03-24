n=int(input())
l=[]
cnt=0

for i in range(n):
    k=int(input())
    l.append(k)

for i in range(len(l)):
    if l[i]>0:
        cnt+=1
print(cnt)