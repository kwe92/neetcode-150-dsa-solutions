def search(nums: list[int], target: int) -> int:
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (r + l) // 2

        if nums[mid] == target:
            return mid

        # if left is the sorted side
        if nums[mid] >= nums[l]:
            # is the target within the range?
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1


if __name__ == '__main__':
    # Example 1:

    nums = [3, 4, 5, 6, 1, 2]
    target = 1

    # Output: 4
    # Example 2:

    # nums = [3, 5, 6, 0, 1, 2]
    # target = 4

    # Output: -1

    print(search(nums, target))
