
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


def linked_list_to_list(head: ListNode):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def mergeTwoLists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        # choose which node is next to be linked
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        # move to next node so a link can be added
        tail = tail.next

    # assign remainders
    if list1:
        tail.next = list1

    if list2:
        tail.next = list2

    return dummy.next


if __name__ == '__main__':
    # Example 1:
    list1 = build_linked_list([1, 2, 4])
    list2 = build_linked_list([1, 3, 5])
    result1 = mergeTwoLists(list1, list2)
    print(f"Example 1 Output: {linked_list_to_list(result1)}")
    # Expected Output: [1, 1, 2, 3, 4, 5]

    # Example 2:
    list1 = build_linked_list([])
    list2 = build_linked_list([1, 2])
    result2 = mergeTwoLists(list1, list2)
    print(f"Example 2 Output: {linked_list_to_list(result2)}")
    # Expected Output: [1, 2]

    # Example 3:
    list1 = build_linked_list([])
    list2 = build_linked_list([])
    result3 = mergeTwoLists(list1, list2)
    print(f"Example 3 Output: {linked_list_to_list(result3)}")
    # Expected Output: []
