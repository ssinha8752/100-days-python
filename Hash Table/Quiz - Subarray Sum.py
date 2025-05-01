def subarray_sum(l,t):
    dict = {0:-1}
    s=0
    for j, i in enumerate(l):
        s+=i
        if s-t in dict:
            return [dict[s-t]+1, j]
        dict[s] = i
    return []


nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
