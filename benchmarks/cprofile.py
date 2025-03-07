import cProfile
import pstats
from os import path, makedirs

def profile_function(func):
    def wrapper(*args, **kwargs):
        directory = 'benchmarks/results/before'

        if not path.exists(directory):
            makedirs(directory)

        profiler = cProfile.Profile()
        profiler.enable()

        result = func(*args, **kwargs)

        profiler.disable()

        filename = path.join(directory, f"{func.__name__}_stats.prof")
        
        stats = pstats.Stats(profiler)
        stats.dump_stats(filename)

        print(f"Finished profiling, saved file as '{filename}'.")
        return result
    return wrapper




