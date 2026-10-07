# Failing

def isValid(s: str) -> bool:
    valid_char = ['(', ')', '{', '}', '[', ']']

    l = 0
    r = len(s) - 1

    res = False

    while r < len(s):
        open = s[l]
        closed = s[r]
        if open == '(' and closed == ')' or l+1 <= len(s)-1 and (open == '(' and s[l+1] == ')'):
            res = True
            l += 1
            r += 1
        elif open == '{' and closed == '}' or l+1 <= len(s) - 1 and (open == '{' and s[l+1] == '}'):
            res = True
            l += 1
            r += 1
        elif open == '[' and closed == ']' or l+1 <= len(s) - 1 and (open == '[' and s[l+1] == ']'):
            res = True
            l += 1
            r += 1
        else:
            res = False
            l += 1
            r += 1

    return res


if __name__ == '__main__':
    # Example 1:

    s = "[]"
    # Output: true

    # Example 2:

    # s = "([{}])"
    # Output: true

    # Example 3:

    s = "[(])"
    # Output: false

    print(isValid(s))
