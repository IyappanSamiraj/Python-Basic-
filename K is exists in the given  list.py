#Given 2 numbers N and K followed by elements of N .Print 'yes' if K exists else print 'no'.


n,k=map(int,input().split())
lst=list(map(int,input().split()))
su=0
for i in range(0,len(lst)):
    if k == i:
        su+=1
if su>0:print('yes')
else:print('no')
