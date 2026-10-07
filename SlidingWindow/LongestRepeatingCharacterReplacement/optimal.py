def characterReplacement(s: str, k: int) -> int:
    char_count = {}
    res = 0
    l = 0

    for r in range(len(s)):
        char_count[s[r]] = 1 + char_count.get(s[r], 0)
        while (r - l + 1) - max(char_count.values()) > k:
            char_count[s[l]] -= 1
            l += 1
        res = max(res, (r - l + 1))
    return res


if __name__ == '__main__':
    # s = "XYYX"
    # k = 2
    # # Output: 4

    s = "AAABABB"
    k = 1
    # Output: 5

    print(characterReplacement(s, k))
