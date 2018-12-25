# class Solution(object):

def findKth(A, B, k):
    if len(A) == 0:
        return B[k - 1]
    if len(B) == 0:
        return A[k - 1]
    if k == 1:
        return min(A[0], B[0])

    # a = A[k // 2 - 1] if len(A) >= k // 2 else None
    # b = B[k // 2 - 1] if len(B) >= k // 2 else None

    # if b is None or (a is not None and a < b):
    # return findKth(A[k // 2:], B, k - k // 2)

    # return findKth(A, B[k // 2:], k - k // 2)  # 这里要注意：因为 k/2 不一定 等于 (k - k/2)

    if len(B) <= k // 2:
        return findKth(A[k // 2:], B, k - k // 2)
    # a = A[k // 2 - 1]
    # b = B[k // 2 - 1]
    elif (len(A) >= k//2 and A[k // 2 - 1] < B[k // 2 - 1]):
        return findKth(A[k // 2:], B, k - k // 2)

    elif len(A) <= k // 2:
        return findKth(A, B[k // 2:], k - k // 2)
    # a = A[k // 2 - 1]
    # b = B[k // 2 - 1]
    elif (len(B) >= k//2 and A[k // 2 - 1] > B[k // 2 - 1]):
        return findKth(A[k // 2:], B, k - k // 2)

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    n = len(nums1) + len(nums2)
    if n % 2 == 1:
        return findKth(nums1, nums2, n // 2 + 1)
    else:
        smaller = findKth(nums1, nums2, n // 2)
        bigger = findKth(nums1, nums2, n // 2 + 1)
        return (smaller + bigger) / 2.0

if __name__ == '__main__':
   # mm = Solution()
    A = [1,2,3]
    B = [5,6,7]
    ss = findMedianSortedArrays(A , B)
    print(ss)
