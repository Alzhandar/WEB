x=int(input())
d=int(input())

s=str(x)
s2=str(d)
cnt=0

for chr in s:
    if chr==s2:
        cnt+=1
    
print(cnt)