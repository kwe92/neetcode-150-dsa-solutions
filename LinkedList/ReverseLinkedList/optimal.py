class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode | None) -> ListNode | None:
    prev = None
    curr = head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


if __name__ == '__main__':
    # Example 1:

    head = [0, 1, 2, 3]

    # Output: [3,2,1,0]
    # Example 2:

    # head = []

    # Output: []

    print(reverseList(head))
