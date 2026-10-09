def search(nums: list[int], target: int) -> int:
    l = 0
    r = len(nums) - 1
    default = -1

    while l <= r:

        mid = (l + r) // 2

        if nums[mid] == target:
            return mid

        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1  # throw away right side
            else:
                l = mid + 1  # throw away left side
        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1

    return default


if __name__ == '__main__':
    # Example 1:

    nums = [3, 4, 5, 6, 1, 2]
    target = 1

    # Output: 4

    # Example 2:

    # nums = [3, 5, 6, 0, 1, 2]
    # target = 4

    # Output: -1

    # nums = [5, 1, 2, 3, 4]
    # target = 1

    # nums = [3, 4, 5, 6, 1, 2]
    # target = 1

    print(search(nums, target))


# def search(nums: list[int], target: int) -> int:
#     l = 0
#     r = len(nums) - 1
#     default = -1

#     while l <= r:
#         if nums[l] == target:
#             return l
#         if nums[r] == target:
#             return r

#         mid = (l + r) // 2

#         if nums[mid] == target:
#             return mid
#         if nums[mid] < target or nums[l] > target:
#             l = mid + 1
#         else:
#             r = mid - 1
#     return default
