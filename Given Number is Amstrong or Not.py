num=int(input())
iyps=0
temp=num
while (temp>0):
    guvi = temp % 10
    iyps = iyps + guvi ** 3
    temp //= 10
if num==iyps:
    print('Amstrong number')
else:
    print('not Amstrong number')
