from tqdm import tqdm
import json
import yaml
import numpy as np

function_name = "strongPasswordChecker"

def read_parameters():
    with open(f"leetcode/config/test_cases/config_test_cases_for_{function_name}.yaml", 'r') as f:
        parameters = yaml.safe_load(f)
    return parameters
    

def get_random_string(min_size, max_size, letters):
    out = ''.join(np.random.choice(list(letters), np.random.randint(min_size, max_size + 1)))
    return out


def is_strong_password(password):
    # 6 <= len <= 20
    if not 6 <= len(password) <= 20:
        return False
    # one lowercase, one upper case, one digit, not three repeating
    cond_upper = False
    cond_lower = False
    cond_digit = False
    cond_repeating = False
    last_chars = [None, None, None]
    for char in password:
        if char.isupper():
            cond_upper = True
        if char.islower():
            cond_lower = True
        if char in "0123456789":
            cond_digit = True
        last_chars[:2] = last_chars[1:]
        last_chars[2] = char
        if all(i == last_chars[0] for i in last_chars):
            return False
    if not (cond_upper and cond_lower and cond_digit):
        return False
    return True


def get_distance_to_closer_strong_password(password):
    cond_digit = False
    cond_upper = False
    cond_lower = False
    to_remove = 0
    last_chars = [None, None, None]
    for index, char in enumerate(password):
        if not cond_digit and char in "0123456789":
            cond_digit = True
        if not cond_upper and char.isupper():
            cond_upper = True
        if not cond_lower and char.islower():
            cond_lower = True
        last_chars[:2] = last_chars[1:]
        last_chars[2] = char
        if all(i == last_chars[0] for i in last_chars):
            to_remove += 1
    steps = 0
    length = len(password)
    # removing three consecutives (removing = one step)
    steps += to_remove
    length -= to_remove
    # adding essentials if not (replace = one step, adding = one step)
    if not cond_digit:
        steps += 1
        if length < 6:
            length += 1
    if not cond_upper:
        steps += 1
        if length < 6:
            length += 1
    if not cond_lower:
        steps += 1
        if length < 6:
            length += 1
    # removing if too long (not those that are essential) (removing = one step)
    if length > 20:
        steps += length - 20
    # Adding if too short
    if length < 6:
        steps += 6 - length
    return steps


known_test_cases = [
        ["a", 5],
        ["aA1", 3],
        ["1337C0d3", 0],
        ["aaa111", 2],
        ["111111", 2],
        ["11a111", 1],
        ["11a1A1", 0],
        ["aaaaaaaa", 2],
        ["aa1aaBaa", 0],
        ["aaaaaaaaaa", 3],
        ["aa1aaAaa1aa", 0],
        ["aaaaaaaaaaa", 3],
        ["aaaaaaaaaaaaaaaaaaaa", 6],
        ["aa1aaAaaAaaAaaAaaAaa", 0],
        ["aaaaaaaaaaaaaaaaaaaaaa", 8],
        ["aaaB1", 1],
        ["aaaaaaaaaaaaaaaaaaaa0A", 8],
        ["bbaaaabbaabbaabbabba0A", 2],
        ["bbaaaabbaabbaabbaaaa0A", 3],
        ["aaaaAAAAAA000000123456", 5],
        ["FFFFFFFFFFFFFFF11111111111111111111AAA", 23],
        ["bbaaaaaaaaaaaaaaacccccc", 8]
        # bbaaaaaaaaaaaaaaacccccc 0
]


def generate_test_cases():
    parameters = read_parameters()
    test_cases = []
    #nb_test_cases = parameters["nb_test_cases"]
    #min_size = parameters["min_size"]
    #max_size = parameters["max_size"]
    #letters = parameters["letters"]
    for tc in tqdm(known_test_cases):
        test_cases.append(tc)
    test_cases_dict = {
        "input": 1,
        "output": 1,
        "get_size": "len",
        "test_cases": test_cases
    }
    with open(f"test_cases/test_cases_for_{function_name}.json", 'w') as f:
        json.dump(test_cases_dict, f, indent=4)



