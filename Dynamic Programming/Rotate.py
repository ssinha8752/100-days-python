def rotate(nums, k):
    n = len(nums)
    k = k % n
    nums[:] = nums[-k:] + nums[:-k]

nums = [1, 2, 3, 4, 5]
k = 2
rotate(nums, k)
print("Rotated array:", nums)

"""
    EXPECTED OUTPUT:
    ----------------
    Rotated array: [5, 6, 7, 1, 2, 3, 4]

"""