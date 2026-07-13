
# TODO:  Understand why text books chose the merge_somewhat_optimal way
# TODO^: as there is no need for two while loops and complicated conditionals

# Solutions that I figured out with AI and studied
def merge_optimal(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # Set pointers for the end of nums1's valid elements, nums2, and nums1's write space
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        # Loop only depends on p2. If p2 < 0, we are finished.
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                # This block handles both normal merging AND the nums2 cleanup
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

def merge_somewhat_optimal(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    # Set pointers for the end of nums1's valid elements, nums2, and nums1's write space
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    # Compare elements from the back and move the larger one to the write position
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # If there are remaining elements in nums2, copy them over.
    # (If there are remaining elements in nums1, they are already in their correct places)
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1