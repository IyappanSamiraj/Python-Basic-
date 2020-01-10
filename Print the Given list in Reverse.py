'''You are given with a queue. Your task is to reverse the queue elements and print it.'''

n=int(input())
num=list(map(int,input().split()))
m=num[::-1]
print(*m)
