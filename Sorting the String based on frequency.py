'''Given a string 'S', sort the characters based on the frequency(highest and lowest) and print the resultant string.(Note:If the frequency of different character is same then sort based on alphabetical order).
Input Size : 1 <= S <= 100000

Sample Testcases :
INPUT
aabbba

OUTPUT
aaabbb'''

n=str(input())
s = set()
list = []
for ch in n:
    if ch not in s:
        s.add(ch)
        list.append(ch)
m=''.join(list)
print(m)
