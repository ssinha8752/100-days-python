counter=0
memo=[None]*100
def fib(n):
    global  counter
    counter+=1
    if memo[n] is not None:
        return memo[n]
    if n==0 or n==1:
        return n
    memo[n]= fib(n-1)+fib(n-2)
    return memo[n]

# Example usage

print(fib(7))  # Output: 55
print(counter) # O(2n-1)