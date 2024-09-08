def solve(i,curr):
    if i==n:
        if curr==s:
            return True
        return False
    skip=solve(i+1,curr)
    take=solve(i+1,curr+dic[i])
    return take or skip

n = 6
s = "ilikesung"
dic = ["i", "like", "sam", "sung", "samsung", "mobile"]
print(int(solve(0,'')))
