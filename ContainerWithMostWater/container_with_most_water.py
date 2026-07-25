def maxArea(heights: list[int]) -> int:
    largest_area = 0

    i = 0
    j = (len(heights) - 1)

    while i < j:
        distance = j - i
        min_bar = min(heights[i], heights[j])
        current_area = distance * min_bar

        if heights[i] < heights[j]:
            i += 1
            largest_area = max(largest_area, current_area)
            continue
        if heights[i] > heights[j]:
            j -= 1
            largest_area = max(largest_area, current_area)
            continue
        i += 1
        j -= 1
        largest_area = max(largest_area, current_area)

    return largest_area


if __name__ == '__main__':
    height = [1, 7, 2, 5, 4, 7, 3, 6]
    # height = [1, 7, 2, 5, 12, 3, 500, 500, 7, 8, 4, 7, 3, 6]
    print('result:', maxArea(height))
