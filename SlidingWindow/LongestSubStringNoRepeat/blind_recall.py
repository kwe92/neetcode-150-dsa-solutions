def lengthOfLongestSubstring(s: str) -> int:
    l = 0
    window_state: set[str] = set()
    res = 0

    for r in range(len(s)):
        while s[r] in window_state:
            window_state.remove(s[l])
            l += 1
        window_state.add(s[r])
        res = max(res, len(window_state))
    return res


if __name__ == '__main__':
    # s = "zxyzxyz"
    # Output: 3

    s = "pwwkew"
    # Output: 3

    print(lengthOfLongestSubstring(s))
