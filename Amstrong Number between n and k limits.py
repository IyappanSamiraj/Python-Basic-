n,k=map(int,input().split())
for i in range(n+1,k):
    iyps=0
    temp=i
    while(temp>0):
        guvi = temp % 10
        iyps = iyps + guvi ** 3
        temp //= 10
    if i==iyps:
        print(i,end=" ")
