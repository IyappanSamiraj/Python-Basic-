'''Let P represent Paper, R represent Rock and S represent Scissors. Given 2 out of the 3 determine which one wins. If its a draw print 'D'.
Sample Testcase :
INPUT
R P
OUTPUT
P'''

N,M=map(str,input().split())
if N=='P' and M=='R':
	print('P')
elif N=='R' and M=='P':
	print('P')
elif N=='S' and M=='R':
	print('R')
elif N=='R' and M=='S':
	print('R')
elif N=='P' and M=='S':
	print('S')
elif N=='S' and M=='P':
	print('S')
else:
	print("D")
