from tqdm import tqdm
import json
import yaml
import numpy as np

def read_parameters():
    with open("leetcode/config/test_cases/config_test_cases_for_threeSum.yaml", 'r') as f:
        parameters = yaml.safe_load(f)
    return parameters


def get_random_input(parameters):
    max_len = parameters["max_len"]
    min_len = parameters["min_len"]
    max_val = parameters["max_val"]
    min_val = parameters["min_val"]
    lenght = np.random.randint(min_len, max_len)
    nums = np.random.randint(min_val, max_val, lenght)
    nums = [int(i) for i in nums]
    return nums


def brute_force_solution(nums):
    triplets = []
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    new_triplet = sorted([nums[i], nums[j], nums[k]])
                    if new_triplet not in triplets:
                        triplets.insert(0, new_triplet)
    return sorted(triplets)

known_test_cases = [
    [[-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]],
    [[0, 1, 1], []],
    [[0, 0, 0], [[0, 0, 0]]],
    [3000*[0], [[0, 0, 0]]],
    [[-1,0,1,0], [[-1,0,1]]],
    [[-1,0,1,2,-1,-4,-2,-3,3,0,4], [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]],
    [[-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6], [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]]
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
    with open("test_cases/test_cases_for_threeSum.json", 'w') as f:
        json.dump(test_cases_dict, f)



