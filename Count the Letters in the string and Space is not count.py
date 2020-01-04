s=str(input())
sum=0
for n in s:
    if n.isspace()!=True:
        sum=sum+1
print(sum)
