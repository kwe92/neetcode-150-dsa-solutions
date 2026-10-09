# O(log N)
def search(nums: list[int], target: int) -> int:
    try:
        return nums.index(target)
    except:
        return -1


if __name__ == '__main__':
    # Example 1:

    nums = [3, 4, 5, 6, 1, 2], target = 1

    # Output: 4
    # Example 2:

    # nums = [3,5,6,0,1,2], target = 4

    # Output: -1

    print(search(nums, target))
