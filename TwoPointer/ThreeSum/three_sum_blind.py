def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()  # sort array to do teo sum
    length = len(nums)
    seen = set()
    result = []
    for i in range(0, length):
        # skip duplicate starting elements
        if i > 0 and nums[i] == nums[-1]:
            continue
        j = i + 1
        k = length - 1
        # calculate current element plus two sum
        while j < k:
            if nums[i] + nums[j] + nums[k] > 0:
                k -= 1
                continue
            if nums[i] + nums[j] + nums[k] < 0:
                j += 1
                continue
            if (nums[i],  nums[j], nums[k]) not in seen:
                seen.add((nums[i],  nums[j], nums[k]))
                result.append([nums[i], nums[j], nums[k]])
            j += 1

    return result


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    # Expected output: [[-1,-1,2],[-1,0,1]]

    # nums = [0, 1, 1]
    # Expected output: []

    print('result:', threeSum(nums))
