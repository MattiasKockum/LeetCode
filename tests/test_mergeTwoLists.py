import pytest
import json

from leetcode.solutions.mergeTwoLists import Solution
from leetcode.test_cases_generator.generate_test_cases_for_mergeTwoLists import ListNode, make_ll, equal_ll


def read_test_cases():
    with open("test_cases/test_cases_for_mergeTwoLists.json", 'r') as file:
        test_cases = json.load(file)
    return test_cases["test_cases"]

S = Solution()
@pytest.mark.parametrize("list1, list2, expected_result", read_test_cases())
def test_mergeTwoLists(list1, list2, expected_result):
    assert equal_ll(S.mergeTwoLists(make_ll(list1), make_ll(list2)), make_ll(expected_result))

