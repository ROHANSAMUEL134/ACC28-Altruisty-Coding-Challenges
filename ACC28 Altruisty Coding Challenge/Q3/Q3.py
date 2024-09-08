def issteppingnumber(num):
    prev=-1
    while num:
        if prev!=-1 and abs(prev-num%10)!=1:
            return False
        prev=num%10
        num//=10
    return True

n=100
m=500
for num in range(n,m+1):
    if issteppingnumber(num):
        print(num,end=" ")
