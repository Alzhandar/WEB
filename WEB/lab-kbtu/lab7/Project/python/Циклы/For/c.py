a=int(input())
b=int(input())

i=1
while i*i<a:
    i+=1

for j in range(i,b+1):
    if j*j>b:
        break
    print(j*j,end=' ')
