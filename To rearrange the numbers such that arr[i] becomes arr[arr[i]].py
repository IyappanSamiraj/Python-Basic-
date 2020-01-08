#You are given with a list of size ‘n’. The list is imposed with a condition that all elements must be of range 0 to n-1.Your task is to rearrange the numbers such that arr[i] becomes arr[arr[i]].

n=int(input())
lst=list(map(int,input().split()))
a=[]
for i in range(0,n):
    m=lst[i]
    a.append(lst[m])
print(*a)

///Sample Input :
5
4 0 2 1 3
Sample Output :
3 4 2 0 1///
    
    
