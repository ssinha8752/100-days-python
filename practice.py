def myfunc(*args):
    ans=[]
    for i in args:
        if i%2==0:
            ans.append(i)
    return ans

print(myfunc(5,6,7,8))