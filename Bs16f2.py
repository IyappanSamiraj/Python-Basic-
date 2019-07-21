num1,num2=map(int,input().split())
for i in range(num1+1, num2):
    if i>1:
        for num in range(2,i):
            if (i % num) == 0:
                break
        else:
            print(i,end=" ")
