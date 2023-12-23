import pytest
import json
import numpy as np
from leetcode.find_median_of_two_sorted_lists import findMedianSortedArrays

def generate_test_cases():
    with open("tests/test_cases_find_median_of_two_sorted_lists.json", 'w') as f:
        f.write('{"tests": [\n')
        for i in range(1000):
            L1 = sorted(np.random.randint(-100, 100, np.random.randint(20)))
            L2 = sorted(np.random.randint(-100, 100, np.random.randint(20)))
            if L1 == [] and L2 == []:
                continue
            L3 = sorted(L1 + L2)
            l = len(L3)
            if l % 2 == 1:
                median = L3[int(l/2)]
            else:
                print(l, L3)
                median = (L3[int(l/2) - 1] + L3[int(l/2)]) / 2
            f.write(f"\t[{L1}, {L2}, {median}]")
            if i != 999:
                f.write(",\n")
        f.write(']}')


def read_test_cases():
    with open("tests/test_cases_find_median_of_two_sorted_lists.json", 'r') as file:
        test_cases = json.load(file)
    return test_cases["tests"]


@pytest.mark.parametrize("nums1, nums2, expected_result", read_test_cases())
def test_find_median_of_two_sorted_lists (nums1, nums2, expected_result):
    assert findMedianSortedArrays(nums1, nums2) == expected_result
