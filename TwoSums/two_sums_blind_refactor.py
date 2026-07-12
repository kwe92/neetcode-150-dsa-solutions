# TODO: Refactor example: Two Sum Hash Map Technique Explained | must be doable blind
def two_sum(nums: list[int], target: int):
    num_index_map = {}

    for i, num in enumerate(nums):
        if target - num in num_index_map:
            return [num_index_map[target - num], i]
        else:
            num_index_map[nums[i]] = i


if __name__ == '__main__':
    nums = [3,5,8,4]
    target = 7
    print(two_sum(nums, target))