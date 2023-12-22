import pytest
from leetcode.find_median_of_two_sorted_lists import findMedianSortedArrays

@pytest.mark.parametrize("nums1, nums2, expected_result", [
    ([], [1], 1),
    ([1], [], 1),
    ([1], [1], 1),
    ([1], [1, 2], 1),
    ([1, 2], [3, 4], 2.5),
    ([2,2,4,4], [2,2,4,4], 3)
])
def test_find_median_of_two_sorted_lists (nums1, nums2, expected_result):
    assert findMedianSortedArrays(nums1, nums2) == expected_result