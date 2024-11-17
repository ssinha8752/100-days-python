def myfunc(*args):
    ans=[]
    for i in args:
        if i%2==0:
            ans.append(i)
    return ans

print(myfunc(-2,4))


def fun(word):
    res=''
    for i,v in enumerate(word):
        if i%2==0:
            res+=v.upper()
        else:
            res+=v.lower()
    print(res)

fun('Shubham')