class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head: ListNode | None) -> None:
    slow = head
    fast = head.next

    # find middle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # next node from middle is the start of our second linked-list
    second = slow.next

    # sever the second half of the linked-list from head
    slow.next = None

    # reverse the second half
    prev = None
    while second:
        nxt = second.next
        second.next = prev
        prev = second
        second = nxt

    first = head

    # point second to reverse linked-list half
    second = prev

    while second:
        # save nodes before overwriting pointer
        temp1 = first.next
        temp2 = second.next
        # weave the second node into the first linked-list
        first.next = second
        second.next = temp1
        # move to the next iteration
        first = temp1
        second = temp2
