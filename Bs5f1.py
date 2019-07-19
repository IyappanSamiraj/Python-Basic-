num1,num2,num3=input().split()
if num1>num2 and num1>num3:
	d=num1
elif num2>num1 and num2>num3:
	d=num2
else:
	d=num3
print('',d)
