
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Working


def removeNthFromEnd(head: ListNode | None, n: int) -> ListNode | None:
    dummy = ListNode(0, head)
    left = dummy
    right = head

    while n > 0 and right:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next

    return dummy.next


if __name__ == '__main__':
    pass
