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

args = parser.parse_args()


if args.function != None:
    function = args.function[0].split('/')[-1].split('.')[0]
    if args.generate_test_cases:
        print("generating test cases...")
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
        print("profiling...")
        plot_performances(function)
        print(f"profiling done at profiles/{function}.png")

