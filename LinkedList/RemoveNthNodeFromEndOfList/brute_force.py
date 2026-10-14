
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Working; but can be done without reversing the linked-list in the optimal solution


def removeNthFromEnd(head: ListNode | None, n: int) -> ListNode | None:

    if not head:
        return None

    prev = None
    curr = head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    rev_head = prev
    prev = None

    while rev_head:
        if n == 1:
            nxt = rev_head.next
            rev_head.next = prev
            prev = rev_head.next  # skip node
            rev_head = nxt

        else:
            nxt = rev_head.next
            rev_head.next = prev
            prev = rev_head
            rev_head = nxt
        n -= 1

    res = prev

    return res


if __name__ == '__main__':
    pass
