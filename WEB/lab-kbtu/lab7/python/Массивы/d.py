n=int(input())
l=[]
cnt=0

for i in range(n):
    k=int(input())
    l.append(k)

for i in range(len(l)-1):
    if l[i+1]>l[i]:
        cnt+=1

print(cnt)