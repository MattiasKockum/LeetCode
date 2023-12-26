import pytest
import json

from leetcode.solutions.twoSum import Solution


def read_test_cases():
    with open("test_cases/test_cases_for_twoSum.json", 'r') as file:
        test_cases = json.load(file)
    return test_cases["test_cases"]

S = Solution()
@pytest.mark.parametrize("nums, target, expected_result", read_test_cases())
def test_findMedianSortedArrays(nums, target, expected_result):
    assert S.twoSum(nums, target) == expected_result

