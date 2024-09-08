prices=[1,4,5,3,2,1,6]
money=6
l=res=cost=0
for r in range(len(prices)):
    cost+=prices[r]
    if cost>money:
        cost-=prices[l]
        l+=1
    if cost<=money:
        res=max(res,r-l+1)
print(res)
