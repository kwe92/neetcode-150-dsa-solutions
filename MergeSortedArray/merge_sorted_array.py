# Leetcode: 88. Merge Sorted Array

# My solutions
# TODO: in your own words explain why merge_incorrect is True in comments bellow based on your notes
def merge_incorrect(nums1: list[int], m: int, nums2: list[int], n: int) -> None:

        nums1 = nums1[:m]

        nums1 = nums1 + nums2

        nums1.sort()

        print(nums1)

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:

        nums1[:] = nums1[:m] # Time Complexity: O(m + n) | Space Complexity: O(m + n)

        nums1[:] = nums1 + nums2 # Time Complexity: O(m + n) | Space Complexity: O(m + n)

        nums1.sort() # Time Complexity: O((m + n) * log(m + n)) | Space Complexity: O(m + n)

        print(nums1)

def merge_optimal(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

if __name__ == '__main__':

    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    n = 3
    m = 3

    merge(nums1, m, nums2, n)

    print(f'external nums1: {nums1}')

# 88. Merge Sorted Array — Key Constraints & Logic

#   - Inputs & Base Cases

#       - Given two arrays in ascending (non-decreasing) order.
#         nums1 has a length of m + n. If m = 0 or n = 0 (base cases), there are no
#         trailing zeros; otherwise, nums1 has n trailing zeros.

#   - Time Complexity O(m+n)
# 
#       - Because the arrays are already sorted, we do not
#         need to resort them with Python's built-in Timsort. We can use index pointer
#         math to adjust the arrays in linear time O(m+n), or O(N). While index
#         assignment happens in constant time, traversal is linear because we must
#         traverse the entire array and cannot split it logarithmically (like binary
#         search).

#   - Space Complexity O(1)

#       - The index pointer approach avoids creating temporary
#         arrays. In slicing and concatenation (like nums1[:m] or nums1 + nums2), the
#         right-hand side expressions allocate new temporary objects in RAM. The
#         pointer approach bypasses this by modifying nums1 directly in-place.


