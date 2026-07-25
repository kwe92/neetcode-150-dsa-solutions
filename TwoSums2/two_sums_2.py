def twoSum(numbers: list[int], target: int) -> list[int]:
    length = len(numbers)

    i = 0
    j = length - 1

    while i < j:
        if (numbers[i] + numbers[j]) > target:
            j -= 1
            continue
        if (numbers[i] + numbers[j]) < target:
            i += 1
            continue
        return [i + 1, j + 1]


if __name__ == '__main__':
    numbers = [1, 3, 4, 5, 7, 11]
    target = 9

    print('result:', twoSum(numbers, target))
