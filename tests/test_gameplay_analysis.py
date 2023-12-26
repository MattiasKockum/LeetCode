import pytest
import pandas as pd
import json

from leetcode.solutions.gameplay_analysis import gameplay_analysis


def read_test_cases():
    with open("test_cases/test_cases_for_gameplay_analysis.json", 'r') as file:
        test_cases = json.load(file)
    r = test_cases["test_cases"]
    for i in range(len(r)):
        r[i][0] = pd.DataFrame(r[i][0]).astype({'player_id':'Int64', 'device_id':'Int64', 'event_date':'datetime64[ns]', 'games_played':'Int64'})
        r[i][1] = pd.DataFrame(r[i][1])
    return r

@pytest.mark.parametrize("activity, expected_result", read_test_cases())
def test_findMedianSortedArrays(activity, expected_result):
    assert gameplay_analysis(activity).equals(expected_result)

