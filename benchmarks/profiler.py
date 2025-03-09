from line_profiler import LineProfiler
from os import path, makedirs

def profile_function(func, profile_type='before'):
    def wrapper(*args, **kwargs):
        base_directory = 'benchmarks/results'
        
        directory = path.join(base_directory, profile_type)

        if not path.exists(directory):
            makedirs(directory)

        profiler = LineProfiler()
        profiler.add_function(func)

        result = profiler(func)(*args, **kwargs)

        filename = path.join(directory, f"{func.__name__}_line_stats.lprof")

        with open(filename, 'w') as f:
            profiler.print_stats(stream=f)

        print(f"Finished profiling, saved file as '{filename}'.")
        
        return result
    return wrapper
