n=int(input())
s=0
a=0
b=1
while s<n:
    l=a+b
    a=b
    b=l
    s=s+1
    print(a,end=' ')
