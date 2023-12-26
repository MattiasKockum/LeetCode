from tqdm import tqdm
import numpy as np
import json
import yaml

def read_parameters():
    with open("leetcode/config/test_cases/config_test_cases_for_twoSum.yaml", 'r') as f:
        parameters = yaml.safe_load(f)
    return parameters

def generate_test_cases():
    parameters = read_parameters()
    test_cases = []
    nb_test_cases = parameters["nb_test_cases"]
    min_len = parameters["min_len"]
    max_len = parameters["max_len"]
    min_value = parameters["min_value"]
    max_value = parameters["max_value"]
    nb_test_cases_done = 0
    while nb_test_cases_done < nb_test_cases:
        lenght = np.random.randint(min_len, max_len)
        nums = np.random.randint(min_value, max_value, lenght)

        X, Y = np.meshgrid(nums, nums)

        sum_matrix = X + Y

        unique, counts = np.unique(sum_matrix, return_counts=True)
        count = dict(zip(unique, counts))

        unique_found = False
        # find unique
        for i in count:
            point = np.where(sum_matrix == i)
            point = [int(point[0][0]), int(point[1][0])]
            if count[i] == 2 and point[0] != point[1]:
                unique_found = True
                target = i
                break
        if not unique_found:
            continue

        test_cases.append((nums.tolist(), int(target), point))
        nb_test_cases_done += 1

    test_cases_dict = {
        "input": 2,
        "output": 1,
        "get_size": "len",
        "test_cases": test_cases
    }
    with open("test_cases/test_cases_for_twoSum.json", 'w') as f:
        json.dump(test_cases_dict, f)



