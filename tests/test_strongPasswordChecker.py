import pytest
import json
import numpy as np

from leetcode.solutions.strongPasswordChecker import Solution


def read_test_cases():
    with open("test_cases/test_cases_for_strongPasswordChecker.json", 'r') as file:
        test_cases = json.load(file)
    return test_cases["test_cases"]

S = Solution()
@pytest.mark.parametrize("password, expected_result", read_test_cases())
def test_strongPasswordChecker(password, expected_result):
    assert S.strongPasswordChecker(password) == expected_result
