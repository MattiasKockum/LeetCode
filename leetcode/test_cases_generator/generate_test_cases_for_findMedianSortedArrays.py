from tqdm import tqdm
import json
import yaml
import numpy as np

def read_parameters():
    with open("leetcode/config/test_cases/config_test_cases_for_findMedianSortedArrays.yaml", 'r') as f:
        parameters = yaml.safe_load(f)
    return parameters
    

def slow_find_median(L1, L2):
    L3 = sorted(L1 + L2)
    l = len(L3)
    if l % 2 == 1:
        median = L3[int(l/2)]
    else:
        median = (L3[int(l/2) - 1] + L3[int(l/2)]) / 2
    return median

def generate_test_cases():
    parameters = read_parameters()
    test_cases = []
    for _ in tqdm(range(parameters["nb_test_cases"])):
        L1 = sorted(
                np.random.randint(
                    parameters["min_limit"],
                    parameters["max_limit"],
                    np.random.randint(parameters["size"])
                ).tolist())
        L2 = sorted(
                np.random.randint(
                    parameters["min_limit"],
                    parameters["max_limit"],
                    np.random.randint(parameters["size"])
                ).tolist())
        if L1 == [] and L2 == []:
            continue
        test_cases.append((L1, L2, slow_find_median(L1, L2)))
    test_cases_dict = {
        "input": 2,
        "output": 1,
        "get_size": "len",
        "test_cases": test_cases
    }
    with open("test_cases/test_cases_for_findMedianSortedArrays.json", 'w') as f:
        json.dump(test_cases_dict, f)


