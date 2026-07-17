def productExceptSelf(nums: list[int]) -> list[int]:
    length = len(nums)
    result = [1] * length

    # Pass 1: Calculate the product of all elements to the LEFT of index i
    left_product = 1
    for i in range(length):
        result[i] = left_product
        left_product *= nums[i]

    # Pass 2: Calculate the product of all elements to the RIGHT of index i
    # and multiply it by the existing left product in the result array
    right_product = 1
    for i in range(length - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result
