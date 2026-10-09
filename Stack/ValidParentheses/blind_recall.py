
def isValid(s: str) -> bool:
    stack = []
    closeToOpen = {']': '[', '}': '{', ')': '('}

    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return len(stack) == 0


if __name__ == '__main__':
    # Example 1:

    s = "[]"
    # Output: true

    # Example 2:

    # s = "([{}])"
    # Output: true

    # Example 3:

    # s = "[(])"
    # Output: false

    print(isValid(s))
