
# TODO: Comments are too verbose, should be rewritten in chuncks / phases of code in YOUR OWN WORDS
def merge_optimal(nums1, m, nums2, n):
    p1 = m - 1 # initialized as the index of the last element within the nums1 array that is not a place holder value
    p2 = n - 1 # initialized as the index of the last element within the nums2 array
    p = (m + n) - 1 # initialized as the max index of the nums1 array

    while p2 >= 0: # while nums2 is indexable
        # if nums1 is indexable and the element at the current index of nums1 is greater than
        # the element at the current index of nums2, insert that element in nums1 at index p
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            # decrement the current index winner
            p1 -= 1
        # nums1 is not indexable or the element at the current index of nums2 is greater than or equal to
        # the element at the current index of nums1, so insert that element in nums1 at index p
        else:
            nums1[p] = nums2[p2]
            # decrement the current index winner
            p2 -= 1
        # decrement the insert index regardless of who won
        p -= 1
