class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(arr: list):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def hasCycle(head: ListNode | None) -> bool:

    if not head:
        return False

    curr = head

    val_state = set()

    while curr:
        if curr in val_state:
            return True
        val_state.add(curr)
        curr = curr.next

    if not curr:
        return False
    else:
        return True


if __name__ == '__main__':
    print(hasCycle(build_linked_list([1, 2, 3])))
