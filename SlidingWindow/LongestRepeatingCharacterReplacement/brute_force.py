# Failing and would never work as substrings are contiguous
def characterReplacement(s: str, k: int) -> int:
    char_count_map = {}
    largest = 0

    for c in s:
        if c in char_count_map:
            char_count_map[c] += 1
        else:
            char_count_map[c] = 1

    for key, v in char_count_map.items():
        if v >= k:
            largest = v
            char_count_map.pop(key)
            break

    if len(char_count_map) == 0:
        return len(s)
    return largest + k

    print(char_count_map)


if __name__ == '__main__':
    s = "XYYX"
    k = 2
    # Output: 4

    s = "AAABABB"
    k = 1
    # Output: 5

    print(characterReplacement(s, k))
