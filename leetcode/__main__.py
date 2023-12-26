#!/usr/bin/env python3

"""
Code written by Mattias
On 24/12/2023
The aim of this program is to manage my LeetCode solutions.
"""

import argparse
import importlib
import subprocess

from profile.profile_space_time import plot_performances


parser = argparse.ArgumentParser(
        prog='Mattias',
        description='run the project all once in a single script.'
)

parser.add_argument("-f", "--function", nargs=1, help="Stores the function.")
parser.add_argument("-p", "--profile", action="store_true", help="Profile the function.")
parser.add_argument("-g", "--generate_test_cases", action="store_true", help="Generate test cases for the function.")
parser.add_argument("-t", "--test", action="store_true", help="Tests the function on test cases.")
parser.add_argument("-C", "--create", action="store_true", help="Creates blank files.")

args = parser.parse_args()

def create_challenge(function):
    sources_and_targets = [
        [
            "leetcode/config/blank_solution.txt",
            f"leetcode/solutions/{function}.py"
        ],
        [
            "leetcode/config/blank_test.txt",
            f"tests/test_{function}.py"
        ],
        [
            "leetcode/config/blank_test_cases_config.txt",
            f"leetcode/config/test_cases/config_test_cases_for_{function}.yaml"
        ],
        [
            "leetcode/config/blank_test_cases_generator.txt",
            f"leetcode/test_cases_generator/generate_test_cases_for_{function}.py"
        ]
    ]
    for source, target in sources_and_targets:
        subprocess.run([
            "cp",
            source,
            target])
        subprocess.run([
            "sed", "-i", "-e",
            f"s/function/{function}/g",
            target])

if args.function != None:
    function = args.function[0].split('/')[-1].split('.')[0]
    if args.create:
        create_challenge(function)
        print(f"Successfully created challenge {function}.")
        print(f"Do not forget to git add!")
    if args.generate_test_cases:
        print("Generating test cases...")
        try:
            path = f"test_cases_generator.generate_test_cases_for_{function}"
            module = importlib.import_module(path)
            generate_test_cases_function = module.generate_test_cases
            generate_test_cases_function()
        except ImportError:
            print(f"Error importing module: {path}")
        print("Test cases successfully generated.")
    if args.test:
        subprocess.run(["pytest", f"tests/test_{function}.py"])
    if args.profile:
        print("Profiling...")
        plot_performances(function)
        print(f"Profiling done at profiles/{function}.png")

