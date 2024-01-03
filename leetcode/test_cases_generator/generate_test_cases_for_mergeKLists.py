from tqdm import tqdm
import json
import yaml
import numpy as np

def read_parameters():
    with open("leetcode/config/test_cases/config_test_cases_for_mergeKLists.yaml", 'r') as f:
        parameters = yaml.safe_load(f)
    return parameters


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_random_input(parameters):
    min_size = parameters["min_size"]
    max_size = parameters["max_size"]
    min_val = parameters["min_val"]
    max_val = parameters["max_val"]
    size = np.random.randint(min_size, max_size + 1)
    n = np.random.randint(min_size, size + 1)
    L = None
    for i in range(size):
        val = np.random.randint(min_val, max_val)
        L = ListNode(val, L)
    return [L, n]


def brute_force_solution(self, head, n):
  return 0


def make_ll(l):
    l.reverse()
    L = None
    for i in l:
        L = ListNode(i, L)
    return L


def equal_ll(ll1, ll2):
    node1 = ll1
    node2 = ll2
    if node1 == None and node2 != None:
        return False
    if node2 == None and node1 != None:
        return False
    if node1 == None and node2 == None:
        return True
    elif node1.val == node2.val:
        return equal_ll(node1.next, node2.next)
    else:
        return False


def get_linked_list(ll):
    s = "["
    node = ll
    while node != None:
        s += f"{node.val} "
        node = node.next
    s += "]"
    return s

def print_linked_list(ll):
    print(get_linked_list(ll))


known_test_cases = [
        [[[1, 4, 5], [1, 3, 4], [2, 6]], [1,1,2,3,4,4,5,6]],
        [[], []],
        [[[]], []],
        [[[1,2,4], [1,3,4]], [1,1,2,3,4,4]],
        [[[], []], []],
        [[[], [0]], [0]],
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
    with open("test_cases/test_cases_for_mergeKLists.json", 'w') as f:
        json.dump(test_cases_dict, f)



