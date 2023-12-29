from tqdm import tqdm
import json
import yaml
import numpy as np

def read_parameters():
    with open("leetcode/config/test_cases/config_test_cases_for_maxArea.yaml", 'r') as f:
        parameters = yaml.safe_load(f)
    return parameters


def get_random_input(parameters):
    min_len = parameters["min_len"]
    max_len = parameters["max_len"]
    min_val = parameters["min_val"]
    max_val = parameters["max_val"]
    length = np.random.randint(min_len, max_len)
    random_list = np.random.randint(min_val, max_val, length)
    random_list = [int(i) for i in random_list]
    return list(random_list)


def brute_force_solution(height):
    # Brute Force method
    max_height = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            test_height = min(height[i], height[j]) * (j - i)
            if test_height > max_height:
                max_height = test_height
    return max_height

known_test_cases = [
    [[1,8,6,2,5,4,8,3,7], 49],
    [[1, 1], 1],
    [[0, 1], 0],
    [[0, 1, 0], 0],
    [[1, 2, 1], 2],
    [[2, 1, 1], 2],
    [[2, 2, 1], 2],
    [[2, 1, 2], 4],
    [[2, 2, 2], 4],
    [[1, 8, 1, 1, 1, 1, 8, 1, 7, 1], 49],  # 49 > 40
    [[1, 8, 1, 1, 1, 1, 8, 1, 5, 1], 40],  # 35 < 40
    [[1,10,6,2,5,4,10,3,7], 50],
    [[1, 2, 3, 4, 3, 2, 1], 8],
    [[0, 0, 8, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 24],
]

def generate_test_cases():
    parameters = read_parameters()
    test_cases = []
    nb_test_cases = parameters["nb_test_cases"]
    for test_case in tqdm(known_test_cases):
        test_cases.append(test_case)
    for _ in tqdm(range(nb_test_cases)):
        random_input = get_random_input(parameters)
        output = brute_force_solution(random_input)
        test_cases.append((random_input, output))
    test_cases_dict = {
        "input": 1,
        "output": 1,
        "get_size": "len",
        "test_cases": test_cases
    }
    with open("test_cases/test_cases_for_maxArea.json", 'w') as f:
        json.dump(test_cases_dict, f)



