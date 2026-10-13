class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ! Not Working


def reorderList(head: ListNode | None) -> None:
    if not head:
        return

    dummy = ListNode()
    tail = dummy

    prev = None
    curr = head

    count = 0

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        count += 1 if curr else 0

    rev_head = prev
    curr = head

    for i in range(count):
        if i == 0:
            tail.next = curr
            curr = curr.next
        if i == 1:
            tail.next = rev_head
            rev_head = rev_head.next

        if i % 2:
            tail.next = curr
            curr = curr.next
        else:
            tail.next = rev_head
            rev_head = rev_head.next
        tail = tail.next

    head = dummy.next
