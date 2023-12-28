from tqdm import tqdm
import json
import yaml

def read_parameters():
    with open("leetcode/config/test_cases/config_test_cases_for_longestPalindrome.yaml", 'r') as f:
        parameters = yaml.safe_load(f)
    return parameters

known_test_cases = [
    ["babad", "bab"],
    ["cbbd", "bb"],
    ["bbd", "bb"],
    ["bb", "bb"],
    ["b", "b"],
    ["aba", "aba"],
    ["abaxxvxx", "xxvxx"],
    ["aaxxvxx", "xxvxx"],
    ["aaxxvxxa", "axxvxxa"],
    ["abaxxvxxa", "axxvxxa"],
    ["abaxxvxxab", "baxxvxxab"],
    ["abaxxvxxabqsdqsdqsdqsdqsd", "baxxvxxab"],
    ["ascfxfcsa", "ascfxfcsa"],
    ["zascfxfcsa", "ascfxfcsa"],
    ["aascfxfcsab", "ascfxfcsa"],
    ["ascfxfcsaxbx", "ascfxfcsa"],
    ["xbxascfxfcsa", "ascfxfcsa"],
    ["ascffcsa", "ascffcsa"],
    ["aascffcsab", "ascffcsa"],
    ["ascffcsaxbx", "ascffcsa"],
    ["xbxascffcsa", "ascffcsa"],
    ["ccc", "ccc"]
]

def generate_test_cases():
    parameters = read_parameters()
    test_cases = []
    for test_case in tqdm(known_test_cases):
        test_cases.append(test_case)
    test_cases_dict = {
        "input": 1,
        "output": 1,
        "get_size": "len",
        "test_cases": test_cases
    }
    with open("test_cases/test_cases_for_longestPalindrome.json", 'w') as f:
        json.dump(test_cases_dict, f)



