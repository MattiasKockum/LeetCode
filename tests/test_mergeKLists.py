import pytest
import json

from leetcode.solutions.mergeKLists import Solution
from leetcode.test_cases_generator.generate_test_cases_for_mergeKLists import ListNode, make_ll, equal_ll


def read_test_cases():
    with open("test_cases/test_cases_for_mergeKLists.json", 'r') as file:
        test_cases = json.load(file)
    return test_cases["test_cases"]

S = Solution()
@pytest.mark.parametrize("lists, expected_result", read_test_cases())
def test_mergeKLists(lists, expected_result):
    assert equal_ll(
            S.mergeKLists([make_ll(l) for l in lists]),
            make_ll(expected_result))

