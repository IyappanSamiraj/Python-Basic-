var=str(input())
if (var=='a' or var=='A' or var=='e' or var=='E' or var=='i' or var=='I' or var=='o' or var=='O' or var=='u' or var=='U'):
    print('Vowel')
elif (var>='a' and var<='z') or (var>='A' and var<='Z'):
    print('Consonant')
else:
    print('invalid')
