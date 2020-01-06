n=int(input())
num=list(map(int,input().split()))
sum=0
for i in range(len(num)):
    if(num[i]<0):
        sum=sum+num[i]
print(sum)
