def hasDuplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


if __name__ == '__main__':
    nums = [1, 2, 3, 3]
    print(hasDuplicate(nums))