class Solution(object):
    def merge(self, nums1, m, nums2, n):
        len = m + n -1
        while m and n:
            if nums1[m-1] < nums2[n-1]:
                nums1[len] = nums2[n-1]
                n -= 1
            else:
                nums1[len] = nums1[m-1]
                m -= 1
            len -= 1
        if n > 0:
            nums1[:n] = nums2[:n]