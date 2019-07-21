num1,num2=map(int,input().split())
for i in range(num1,num2+1):
    iyps=0
    temp=i
    while(temp>0):
        guvi = temp % 10
        iyps = iyps + guvi ** 3
        temp //= 10
    if i==iyps:
        print(i,end=" ")
