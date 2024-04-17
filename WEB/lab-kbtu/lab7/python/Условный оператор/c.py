n=int(input())
k=int(input())

s=str(n)

rez=int(s[::-1])-n

if rez==0 and k==1:
    print('YES')
else:
    print('NO')