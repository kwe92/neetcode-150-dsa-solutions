def lengthOfLongestSubstring(s: str) -> int:
    left = 0
    right = 0

    current_longest = 0
    unique_char = set()

    while right < len(s):

        if s[right] not in unique_char:
            unique_char.add(s[right])
            right += 1
            current_longest = max(current_longest, len(unique_char))
        else:
            unique_char.remove(s[left])
            left += 1

    return current_longest


if __name__ == '__main__':
    # s = "zxyzxyz"
    # Output: 3

    # s = "pwwkew"
    # Output: 3

    s = "aabac"
    # Output: 2

    print(lengthOfLongestSubstring(s))


# def lengthOfLongestSubstring(s: str) -> int:
#     unique_char = set()
#     for c in s:
#         unique_char.add(c)
#     print(unique_char)
#     return len(unique_char)

# def lengthOfLongestSubstring(s: str) -> int:
#     left = 0
#     right = 1

#     current_longest = 0

#     unique_char = set()

#     while right < len(s):
#         if len(unique_char) == 0:
#             unique_char.add(s[left])
#         if s[right] not in unique_char:
#             unique_char.add(s[right])
#             right += 1
#         else:
#             unique_char.add(s[right])
#             unique_char.remove(s[left])
#             right += 1
#             left += 1
#         print("unique_char: ", unique_char)
#         current_longest = max(current_longest, len(unique_char))

#     if len(s) > 0 and current_longest == 0:
#         return 1

#     return current_longest
