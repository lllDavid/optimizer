import pstats
from os import path
def compare(file: str, directory: str):
    file_path = path.join(directory, file)
    if path.exists(file_path):
        loaded_stats = pstats.Stats(file_path)
        print(f"\n{directory.capitalize()} stats:")
        
        loaded_stats.sort_stats('cumulative')
        
        loaded_stats.print_stats()

        stats_dict = {}
        
        for func in loaded_stats.fcn_list:
            func_name = func[2]
            stats = loaded_stats.stats.get(func, None)
            if stats:
                calls = stats[0]  
                cumtime = stats[3]  
                stats_dict[func_name] = {'calls': calls, 'cumtime': cumtime}
        
        return stats_dict
    else:
        print(f"{directory.capitalize()} file '{file}' not found!")
        return None

file_name = str(input("Benchmarks to compare:"))

before_stats = compare(file_name, "before")
optimized_stats = compare(file_name, "optimized")

if before_stats and optimized_stats:
    print("\nComparing Function Calls and Cumulative Time:")
    
    for func_name in before_stats:
        if func_name in optimized_stats:
            before_calls = before_stats[func_name]['calls']
            optimized_calls = optimized_stats[func_name]['calls']
            before_cumtime = before_stats[func_name]['cumtime']
            optimized_cumtime = optimized_stats[func_name]['cumtime']
            
            print(f"\nFunction: {func_name}")
            print(f"  Before Calls: {before_calls}, optimized Calls: {optimized_calls}")
            print(f"  Before Cumulative Time: {before_cumtime:.6f}s, optimized Cumulative Time: {optimized_cumtime:.6f}s")
            
            time_change = optimized_cumtime - before_cumtime
            print(f"  Time Change: {time_change:.6f}s")
        else:
            print(f"\nFunction '{func_name}' not found in 'optimized' stats.")

