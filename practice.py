def myfunc(*args):
    ans=[]
    for i in args:
        if i%2==0:
            ans.append(i)
    return ans

print(myfunc(-2,4))