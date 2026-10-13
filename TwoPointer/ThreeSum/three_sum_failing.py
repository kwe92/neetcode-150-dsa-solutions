
# TODO: Look at solution and study it

def threeSum(nums: list[int]) -> list[list[int]]:
    result = {}
    for i in range(0, len(nums)):
        for j in range(i + 1, (len(nums))):
            k = j + 1
            while k < (len(nums)):
                # print(
                #     f'nums[i]: {nums[i]} | nums[j]: {nums[j]} | nums[k]: {nums[k]}')
                if (nums[i] + nums[j] + nums[k]) == 0:
                    result[tuple(sorted([nums[i], nums[j], nums[k]]))] = 1
                k += 1

    return [list(k) for k in result]


if __name__ == '__main__':
    # nums = [-1, 0, 1, 2, -1, -4]
    # output: [[-1,-1,2],[-1,0,1]]

    # nums = [-2, 0, 1, 1, 2]

    nums = [-1, 0, 1, 2, -1, -4]
    # [[-1,-1,2],[-1,0,1]]

    print('result:', threeSum(nums))


#! Failing Brute Force: 1
# result = {}
#     for i in range(0, len(nums)):
#         j = i + 1
#         k = i + 2

#         while k < len(nums):
#             if (nums[i] + nums[j] + nums[k]) == 0:
#                 result[tuple(sorted([nums[i], nums[j], nums[k]]))] = 1
#             j += 1
#             k += 1

#     return [list(k) for k in result]

#! Failing Brute Force: 2 | 25 / 26 passing test cases and time limit exceeded on large input

# def threeSum(nums: list[int]) -> list[list[int]]:
#     result = {}
#     for i in range(0, len(nums)):
#         for j in range(i + 1, (len(nums))):
#             k = j + 1
#             while k < (len(nums)):
#                 # print(
#                 #     f'nums[i]: {nums[i]} | nums[j]: {nums[j]} | nums[k]: {nums[k]}')
#                 if (nums[i] + nums[j] + nums[k]) == 0:
#                     result[tuple(sorted([nums[i], nums[j], nums[k]]))] = 1
#                 k += 1

#     return [list(k) for k in result]
