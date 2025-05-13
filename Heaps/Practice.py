def maximumProduct(nums):
    nums.sort()  # Sort the array in ascending order

    # Case 1: Product of the top three largest values
    option1 = nums[-1] * nums[-2] * nums[-3]

    # Case 2: Product of two smallest values (which may be negative) and the largest value
    option2 = nums[0] * nums[1] * nums[-1]
    return max(option1, option2)

print(maximumProduct([-1,-2,-3]))