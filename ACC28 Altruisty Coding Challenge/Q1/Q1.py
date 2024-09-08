n=2
arr=[1,2,3,2,1,4]
dic={}
for i in arr:
    if i in dic: dic[i]+=1
    else: dic[i]=1
print(*[i for i,j in dic.items() if j==1])
