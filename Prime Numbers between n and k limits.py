n,k=map(int,input().split())
for i in range(n+1, k):
    if i>1:
        for num in range(2,i):
            if (i % num) == 0:
                break
        else:
            print(i,end=" ")
