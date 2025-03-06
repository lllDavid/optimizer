import cProfile
import pstats

from functions.functions import find_large_primes

def run_profiling():
    profiler = cProfile.Profile()
    profiler.enable()

    find_large_primes(1000)

    profiler.disable()

    stats = pstats.Stats(profiler)
    pstats.Stats.dump_stats(stats, "stats.prof")
    print("Finished profiling, saved file.")
    
'''
loaded_stats = pstats.Stats("stats.prof")
loaded_stats.sort_stats('cumulative')  
loaded_stats.print_stats()
'''