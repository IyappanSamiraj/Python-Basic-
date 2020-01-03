username=str(input())
emil=str(input())

#EMAIL
mail=[i for i in emil]
if mail[0].isdigit():
	print('invalid1')
elif mail[6]>='@' and '@' in mail:
	lenn=len(mail)-5
	if mail[lenn+1]=='.' and mail[lenn+2]=='c' and mail[lenn+3]=='o' and mail[lenn+4]=='m':
		print('valid')
	else:
		print('invalid')
else:
	print('invalid')

#PASSWORD
password=str(input())
pas=[word for word in password]
if len(pas)>=8 and len(pas)<=15:
	if pas[0].isupper():
		if 
