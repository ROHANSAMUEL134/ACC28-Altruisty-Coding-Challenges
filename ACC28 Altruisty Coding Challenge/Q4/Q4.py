'''There is a contradiction in this problem sir, in problem statement
you have mentioned answer should not be zero'''
#But the output you provided for the sample input zero
#So let me provide answer for both


s="203"
k=2
removed=0
s=list(s)

#As per the expected output
for i in range(k):
    s.remove(s[i])
print("If answer can be Zero:",''.join(s))


#As per the problem statement i.e answer should not be zero
s="203"
s=list(s)
num_cnt=len(s)-s.count('0')
if num_cnt>k:
    for i in range(k):
        s.remove(temp[i])
else:
    num_cnt-=1
    diff=num_cnt
    i=0
    while num_cnt:
        s.remove(s[i])
        i+=1
        num_cnt-=1
    for i in range(diff):
        s.remove('0')
    
print("If answer can't be Zero:",int(''.join(s)))
