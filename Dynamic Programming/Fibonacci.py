counter=0

def fib(n):
    global  counter
    counter+=1
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)

# Example usage

print(fib(10))  # Output: 55
print(counter)