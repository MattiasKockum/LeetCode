class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        total_length = len(nums1) + len(nums2)
        left_partition_size = (len(nums1) + len(nums2) + 1) // 2
        low, high = 0, len(nums1)

        while low <= high:
            mid1 = (low + high) // 2
            mid2 = left_partition_size - mid1
            
            l1 = nums1[mid1 - 1] if mid1 - 1 >= 0 else float('-inf')
            l2 = nums2[mid2 - 1] if mid2 - 1 >= 0 else float('-inf')
            r1 = nums1[mid1] if mid1 < len(nums1) else float('inf')
            r2 = nums2[mid2] if mid2 < len(nums2) else float('inf')

            if l1 <= r2 and l2 <= r1:
                return max(l1, l2) if total_length % 2 == 1 else (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1

        raise ValueError("Input Not Sorted")
