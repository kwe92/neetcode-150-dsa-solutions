# O(N)
def findMin(nums: list[int]) -> int:
    return min(nums)


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
