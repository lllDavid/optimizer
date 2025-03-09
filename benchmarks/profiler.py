from line_profiler import LineProfiler
from os import path, makedirs

def profile_function(func, profile_type='before'):
    def wrapper(*args, **kwargs):
        base_directory = 'benchmarks/results'
        
        if not path.exists(base_directory):
            makedirs(base_directory)
        
        before_directory = path.join(base_directory, 'before')
        optimized_directory = path.join(base_directory, 'optimized')

        if not path.exists(before_directory):
            makedirs(before_directory)
        
        if not path.exists(optimized_directory):
            makedirs(optimized_directory)

        directory = path.join(base_directory, profile_type)

        if not path.exists(directory):
            makedirs(directory)

        profiler = LineProfiler()
        profiler.add_function(func)

        result = profiler(func)(*args, **kwargs)

        filename = path.join(directory, f"{func.__name__}.lprof")

        with open(filename, 'w') as f:
            profiler.print_stats(stream=f)

        print(f"Finished profiling, saved file as '{filename}'.")

        return result
    return wrapper
