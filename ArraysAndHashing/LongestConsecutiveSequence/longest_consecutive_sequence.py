def longestConsecutive(nums: list[int]) -> int:
    numsSet = set(nums)
    longest = 0

    for n in nums:
        count = 0  # count set to 0 to include the start of a sequence
        if (n - 1) not in numsSet:  # if there is no left neighbor -> represents start of sequence
            while (n + count) in numsSet:  # count current element and all consecutive elements
                count += 1
            longest = max(count, longest)  # update longest consecutive count
    return longest


if __name__ == '__main__':
    # nums = [2, 20, 4, 10, 3, 4, 5]
    # nums = [0, 3, 2, 5, 4, 6, 1, 1]
    nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]

    print('result:', longestConsecutive(nums))

    # Output: 4


# O(nLogn) - Time O(n) - Space: Working Solution

    # accumulator = 0
    # nums = list(set(nums))
    # nums.sort()
    # print(nums)

    # if len(nums) == 0:
    #     return 0

    # i = 1
    # counts = []
    # while i < len(nums):
    #     print(nums[i] - nums[i - 1])
    #     if nums[i] - nums[i - 1] == 1:
    #         accumulator += 1
    #     else:
    #         counts.append(accumulator)
    #         accumulator = 0
    #     i += 1

    # if accumulator > 0:
    #     counts.append(accumulator)

    # counts.sort()

    # if len(counts) == 0:
    #     return 1

    # result = counts[-1]
    # result += 1
    # return result
