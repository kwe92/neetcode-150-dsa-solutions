# O(log N)
def findMin(nums: list[int]) -> int:
    l = 0
    r = len(nums) - 1
    res = nums[l]

    while l <= r:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break

        mid = (l + r) // 2
        res = min(res, nums[mid])

        if nums[mid] >= nums[l]:
            l = mid + 1
        else:
            r = mid - 1
    return res


if __name__ == '__main__':
    # Example 1:

    # nums = [3, 4, 5, 6, 1, 2]

    # Output: 1
    # Example 2:

    # nums = [4,5,0,1,2,3]

    # Output: 0
    # Example 3:

    # nums = [4, 5, 6, 7]

    # Output: 4

    nums = [3, 4, 5, 1, 2]

    print(findMin(nums))
