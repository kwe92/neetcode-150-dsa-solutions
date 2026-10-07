def isValid(s: str) -> bool:
    # array to represent a stack
    stack = []

    # close to open bracket map
    closeToOpen = {')': '(', '}': '{', ']': '['}

    for c in s:
        # if closing bracket
        if c in closeToOpen:
            # ensure there is a corresponding open bracket
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            # if there is no corresponding open bracket return false
            else:
                return False
        # add all open brackets
        else:
            stack.append(c)
    # return true if all open brackets have been closed, false otherwise
    # can also be written as: len(stack) == 0
    return True if not stack else False


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
