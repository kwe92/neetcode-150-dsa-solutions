def isPalindrome(s: str) -> bool:
    normalized_s = ''.join(filter(str.isalnum, s.lower()))
    stop = len(normalized_s) // 2
    i = 0
    j = len(normalized_s) - 1
    while i < stop:
        if normalized_s[i] == normalized_s[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


if __name__ == '__main__':
    s = "Was it a car or a cat I saw?"
    # Output: true

    # s = "tab a cat"
    # Output: false
    print('result:', isPalindrome(s))

# Brute Force: O(n) TIme | O(n) Space


def isPalindrome(s: str) -> bool:
    # filter combined with String Building Pattern to achieve: String Normalization / Sanitization
    normalized_s = ''.join(filter(str.isalnum, s.lower()))
    return normalized_s == ''.join(reversed(normalized_s))
