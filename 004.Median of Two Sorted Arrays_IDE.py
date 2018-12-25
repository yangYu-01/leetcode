# IDE调试版本

#class Solution(object):

def findKth(A, B, k):
    if len(A) == 0:
        return B[k - 1]
    if len(B) == 0:
        return A[k - 1]
    if k == 1:
        return min(A[0], B[0])

    #<原文>
    # a = A[k // 2 - 1] if len(A) >= k // 2 else None
    # b = B[k // 2 - 1] if len(B) >= k // 2 else None

    # if b is None or (a is not None and a < b):
    #     return findKth(A[k // 2:], B, k - k // 2)
    # return findKth(A, B[k // 2:], k - k // 2)  # 这里要注意：因为 k/2 不一定 等于 (k - k/2)
    # </原文>


    #<改写>
    # 把原文1个判断（高手写法），改写成4个判断，容易理解

    # 第1个判断
    if len(B) < k // 2:
        return findKth(A[k // 2:], B, k - k // 2)
    # a = A[k // 2 - 1]
    # b = B[k // 2 - 1]
    elif (len(A) >= k//2 and A[k // 2 - 1] <= B[k // 2 - 1]):
        return findKth(A[k // 2:], B, k - k // 2)

    # 第3个判断
    elif len(A) < k // 2:
        return findKth(A, B[k // 2:], k - k // 2)
    # a = A[k // 2 - 1]
    # b = B[k // 2 - 1]
    elif (len(B) >= k//2 and A[k // 2 - 1] >= B[k // 2 - 1]):
        return findKth(A, B[k // 2:], k - k // 2)
    #</改写>

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
    # answer = Solution()
    output = findMedianSortedArrays(nums1, nums2)
    print(output)

# 错误集锦
#error_1.
    # 第1个判断，elif (len(A) >= k//2 and A[k // 2 - 1] <【=】 B[k // 2 - 1]):
    # 少=，4个if/elif都不进去，nonetype报错。
    # 第4个判断同理。
    # nums1 = [1,1]
    # nums2 = [1,1]
#error_2.
    # 第3个判断elif：return findKth(A, B[k // 2:], k - k // 2)，
    # 第4个判断elif：return findKth(A[k // 2:], B, k - k // 2)，所做操作不一样。第4个判断没改。
    # nums1 = [1,2]
    # nums2 = [-1,3]
#error_3.
    # nums1 = [2]
    # nums2 = [1]
    # 第1个判断，if len(B) <【=】 k // 2:，自己改写，多了一个=，这种情况bigger跳进第一个判断，使bigger=1，结果为1。答案1.5。
    # 第3个判断，elif len(A) <【=】 k // 2:，多了一个=
    # nums1 = [2]
    # nums2 = [1]
