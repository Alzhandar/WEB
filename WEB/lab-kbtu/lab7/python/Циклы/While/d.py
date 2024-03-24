n=int(input())
i=0
found = False

while 2**i<=n:
    if 2**i==n:
        print('YES')
        found = True
        break
    i+=1

if not found:
    print('NO') 