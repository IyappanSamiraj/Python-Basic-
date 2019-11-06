n=str(input())
a=[]
b=[]
for i in n:
	if i not in a:
		a.append(i)
print(len(a))
