from tqdm import tqdm
import json
import yaml
import numpy as np

def read_parameters():
    with open("leetcode/config/test_cases/config_test_cases_for_isValid.yaml", 'r') as f:
        parameters = yaml.safe_load(f)
    return parameters


def get_random_input(parameters):
    min_size = parameters["min_size"]
    max_size = parameters["max_size"]
    min_val = parameters["min_val"]
    max_val = parameters["max_val"]
    return 0


def brute_force_solution(self, x):
  return 0


known_test_cases = [
    ["", True],
    ["()", True],
    ["[]", True],
    ["{}", True],
    ["{}()", True],
    ["{}[]()", True],
    ["{}[()]", True],
    ["{}[()()]", True],
    ["{}[(){}()]", True],
    ["{}[([]){}()]", True],
    ["()((((((()))))))", True],
    ["()(()()(()))", True],
    ["([)]", False],
    ["([)", False],
    ["(", False],
    [")", False],
    ["){", False],
]
input_size = 1
output_size = 1

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
        "input": input_size,
        "output": output_size,
        "get_size": "len",
        "test_cases": test_cases
    }
    with open("test_cases/test_cases_for_isValid.json", 'w') as f:
        json.dump(test_cases_dict, f)



