
def trap(height: list[int]) -> int:
    pass


if __name__ == '__main__':
    height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
    print('result', trap(height))

#! Failing O(n) Time | O(n) Space

# def trap(height: list[int]) -> int:
#     maxLeft = []
#     maxRight = []
#     l_max = 0
#     r_max = 0

#     max_water = 0

#     for i in range(0, len(height)):
#         if i == 0:
#             maxLeft.append(0)
#         if i == (len(height) - 1):
#             maxRight.append(0)
#         else:
#             l_max = max(l_max, height[i - 1])
#             maxLeft.append(l_max)
#             r_max = max(r_max, height[i + 1])
#             maxRight.append(r_max)

#     # print(f'input: {height} | maxLeft: {maxLeft} | maxRight: {maxRight}')
#     print(f'\n{height}\n{maxLeft}')

#     for i in range(0, len(height)):
#         # max_water
#         current_min = min(maxLeft[i], maxRight[i])
#         current_result = current_min - height[i]
#         print(current_result)
#         if current_result > 0:
#             max_water += current_result
#     return max_water
