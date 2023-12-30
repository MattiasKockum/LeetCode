import pytest
import json

from leetcode.solutions.threeSum import Solution


def read_test_cases():
    with open("test_cases/test_cases_for_threeSum.json", 'r') as file:
        test_cases = json.load(file)
    return test_cases["test_cases"]

S = Solution()
@pytest.mark.parametrize("x, expected_result", read_test_cases())
def test_findMedianSortedArrays(x, expected_result):
    assert S.threeSum(x) == expected_result

