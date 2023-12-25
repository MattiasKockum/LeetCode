import matplotlib.pyplot as plt
import sys
import timeit
import memory_profiler
import json
import importlib
from tqdm import tqdm
import pandas as pd

get_size_dict = {
    "len": len,
    "sys.getsizeof": sys.getsizeof
}

def profile_memory_usage(func, *args, **kwargs):
    memory_usage = []
    def profiled_func():
        result = func(*args, **kwargs)
        memory_usage.append(memory_profiler.memory_usage()[0])
        return result
    memory_profiler.profile()(profiled_func)()
    return memory_usage[0]


def measure_space_time_complexity(function_name):
    with open(f"test_cases/test_cases_for_{function_name}.json", 'r') as file:
        test_cases = json.load(file)
    get_size = get_size_dict[test_cases["get_size"]]
    nb_inputs = test_cases["input"]
    test_cases = [tc[:nb_inputs] for tc in test_cases["test_cases"]]
    path = f"solutions.{function_name}"
    module = importlib.import_module(path)
    solution = module.Solution
    function = lambda x: solution.__dict__[function_name](solution, *x)
    size = []
    time_taken = []
    space_array = []
    for test in tqdm(test_cases):
        stdout = sys.stdout
        sys.stdout = open(f"profiles/stdout_{function_name}.out", 'a')
        input_size = sum([get_size(arg) for arg in test])
        start_time = timeit.default_timer()
        memory_used = profile_memory_usage(function, test)
        diff_time = timeit.default_timer() - start_time
        size.append(input_size)
        time_taken.append(diff_time)
        space_array.append(memory_used)
        sys.stdout = stdout
    return size, space_array, time_taken


def plot_performances(function_name, outliers_threshold=0.95):
    # TODO : make faster profiling by taking one test by group of same size
    fig, axs = plt.subplots(1, 2)
    fig.tight_layout()
    size, memory_taken, time_taken = measure_space_time_complexity(function_name)
    # Need to remove some outliers
    data = data = list(zip(size, memory_taken, time_taken))
    df = pd.DataFrame(data,
                      columns=["size", "mem", "time"])
    time_threshold = df['time'].quantile(outliers_threshold)
    memory_threshold = df['mem'].quantile(outliers_threshold)
    filtered_df = df[
            (df['time'] <= time_threshold)
            & (df['mem'] <= memory_threshold)]
    # Plotting
    axs[0].set_title("memory")
    axs[0].scatter(filtered_df["size"], filtered_df["mem"], alpha=0.5)
    axs[1].set_title("time")
    axs[1].scatter(filtered_df["size"], filtered_df["time"], alpha=0.5)
    fig.savefig(f"profiles/{function_name}.png")
    df.to_pickle(f"profiles/{function_name}.pkl")


