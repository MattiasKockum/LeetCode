import pytest
import json

from leetcode.solutions.removeNthFromEnd import Solution
from leetcode.test_cases_generator.generate_test_cases_for_removeNthFromEnd import ListNode, make_ll, equal_ll


def read_test_cases():
    with open("test_cases/test_cases_for_removeNthFromEnd.json", 'r') as file:
        test_cases = json.load(file)
    return test_cases["test_cases"]

S = Solution()
@pytest.mark.parametrize("head, n, expected_result", read_test_cases())
def test_findMedianSortedArrays(head, n, expected_result):
    assert equal_ll(S.removeNthFromEnd(make_ll(head), n), make_ll(expected_result))

