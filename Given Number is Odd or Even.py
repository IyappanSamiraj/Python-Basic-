#get the input
num=int(input())

#Condition is satisfied only the number is divisible by 2
if num%2==0:
    print('Even')

#If else condition Is satisfied at if condition not satisfied 
elif num<0:
    print('Invalid')

#In if and elif Condition not satisfied Default else printed
else:
    print('Odd')
