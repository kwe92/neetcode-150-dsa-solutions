import math

# Optimal O(n) Time | O(1) Space


def productExceptSelf(nums: list[int]) -> list[int]:
    length = len(nums)
    result = [1] * length

    left_prod = 1
    for i in range(length):
        result[i] = left_prod
        left_prod *= nums[i]

    rignt_prod = 1
    for i in range(length - 1, -1, -1):
        result[i] *= rignt_prod
        rignt_prod *= nums[i]

    return result


if __name__ == '__main__':
    nums = [1, 2, 4, 6]
    print(productExceptSelf(nums))

    # Output: [48,24,12,8]

# Brute Force: O(N^2) Time | O(N) Space


def productExceptSelf_brute_force(nums: list[int]) -> list[int]:
    result = []
    length = len(nums)
    for i in range(0, length):
        filtered_nums = []
        if i == 0:
            result.append(math.prod(nums[1:length]))
        else:
            filtered_nums.extend(nums[0:i])
            filtered_nums.extend(nums[i+1:length])
            result.append(math.prod(filtered_nums))
    return result
