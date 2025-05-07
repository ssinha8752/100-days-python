def fib(n):
    a = 0
    b = 1
    if n==0:
        return a
    elif n==1:
        return b
    elif n>1:
        return fib(n-1)+fib(n-2)

print(fib(4))