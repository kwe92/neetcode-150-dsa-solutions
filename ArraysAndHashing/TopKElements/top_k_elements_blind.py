def topKFrequent(nums: list[int], k: int) -> list[int]:
    freq_map: dict[int, int] = {}
    count_array: list[list[int]] = [[] for _ in range(len(nums) + 1)]

    for num in nums:
        # a trick to increment without using if else incase the index does not exist
        freq_map[num] = 1 + freq_map.get(num, 0)

    for num, count in freq_map.items():
        count_array[count].append(num)

    result = []
    for i in range(len(count_array) - 1, 0, -1):
        for num in count_array[i]:
            result.append(num)
            if len(result) == k:
                return result


if __name__ == '__main__':
    # nums = [1, 2, 2, 3, 3, 3]
    nums = [1, 1, 1, 2, 2, 100]

    k = 2

    print('result:', topKFrequent(nums, k))

    # Output: [2,3]
