import pytest
import json
import numpy as np

from leetcode.solutions.findMedianSortedArrays import Solution


def read_test_cases():
    with open("test_cases/test_cases_for_findMedianSortedArrays.json", 'r') as file:
        test_cases = json.load(file)
    return test_cases["test_cases"]

S = Solution()
@pytest.mark.parametrize("nums1, nums2, expected_result", read_test_cases())
def test_findMedianSortedArrays(nums1, nums2, expected_result):
    assert S.findMedianSortedArrays(nums1, nums2) == expected_result
