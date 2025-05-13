def maximumProduct(nums):
    prod=1
    max3=sorted(nums, key=abs, reverse=True)[:-3]
    for i in max3:
        prod=prod*i
    print(max3)
    return prod

print(maximumProduct([-100,-98,-1,2,3,4]))