
def threeSum(nums: list[int]) -> list[list[int]]:
    result = []
    unique_trips = set()
    nums.sort()
    for i in range(0, len(nums)):
        if len(result) > 1 and nums[i] == nums[i - 1]:
            continue
        j = i + 1
        k = (len(nums) - 1)
        while j < k:
            if nums[i] + nums[j] + nums[k] > 0:
                k -= 1
                continue
            if nums[i] + nums[j] + nums[k] < 0:
                j += 1
                continue
            trip_id = (nums[i], nums[j], nums[k])
            if trip_id not in unique_trips:
                unique_trips.add(trip_id)
                result.append([nums[i], nums[j], nums[k]])
            k -= 1
            j += 1
    return result


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]

    # output: [[-1,-1,2],[-1,0,1]]

    # nums = [-2, 0, 1, 1, 2]

    # nums = [-1, 0, 1, 2, -1, -4]
    # [[-1,-1,2],[-1,0,1]]

    nums = [0, 0, 0]

    print('result:', threeSum(nums))
