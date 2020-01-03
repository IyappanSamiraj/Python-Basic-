username=str(input())
emil=str(input())

#EMAIL
mail=[i for i in emil]
if mail[0].isdigit():print('invalid1')
elif mail[6]>='@' and '@' in mail:
	lenn=len(mail)-5
	if mail[lenn+1]=='.' and mail[lenn+2]=='c' and mail[lenn+3]=='o' and mail[lenn+4]=='m':print('valid')
	else:print('invalid')
else:print('invalid')

#PASSWORD
password=str(input())
pas=[word for word in password]
if len(pas)>=8 and len(pas)<=15:
	if pas[0].isupper():
		count=0
		for i in range(0,len(pas)):
			mid=ord(pas[i])
			if (mid>=27 and mid<=47) or (mid>=58 and mid<=64):
				count=count+1
		if count==1:
			coun=0
			for j in range(0,len(pas)):
				nif=ord(pas[j])
				if (nif>=48 and nif<=57):
					coun=coun+1
			if coun>0:print('valid')
			else:print('Enter the valid password')
		else:print('Enter the valid password')
	else:print('Enter the valid password')
else:print('password is too short')
