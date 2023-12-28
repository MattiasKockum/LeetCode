import pytest
import json

from leetcode.solutions.longestPalindrome import Solution


def read_test_cases():
    with open("test_cases/test_cases_for_longestPalindrome.json", 'r') as file:
        test_cases = json.load(file)
    return test_cases["test_cases"]

S = Solution()
@pytest.mark.parametrize("x, expected_result", read_test_cases())
def test_findMedianSortedArrays(x, expected_result):
    assert S.longestPalindrome(x) == expected_result

