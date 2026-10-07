def lengthOfLongestSubstring(s: str) -> int:
    # set initial left pointer state
    l = 0
    # set initial best length state for result
    best = 0

    # state to track window range
    unique_char_state: set[str] = set()

    # set initial right pointer state and move right pointer
    for r in range(len(s)):
        # move left pointer dynamically if the condition is met
        while s[r] in unique_char_state:
            unique_char_state.remove(s[l])
            l += 1

        unique_char_state.add(s[r])
        best = max(best, len(unique_char_state))

    return best


if __name__ == '__main__':
    s = "zxyzxyz"
    # Output: 3

    print(lengthOfLongestSubstring(s))
