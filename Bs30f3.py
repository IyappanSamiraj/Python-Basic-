n1,n2=map(int,input().split())
num1,num2=map(int,input().split())
if n1<num1 or n2<num2:
	h=num1-n1
	m=num2-n2
else:
	h=n1-num1
	m=n2-num2
print(h,m)
