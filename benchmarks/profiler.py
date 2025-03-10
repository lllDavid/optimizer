from io import StringIO
from os import path, makedirs
from statistics import mean
from line_profiler import LineProfiler

profiling_results = []

def save_profiling_result(profile_type, func_name, stats_str):
    base_directory = 'benchmarks/results'
    directory = path.join(base_directory, profile_type)

    if not path.exists(directory):
        makedirs(directory)

    filename = path.join(directory, f"{func_name}.lprof")
    with open(filename, 'w') as f:
        f.write(stats_str)

    result_dict = {
        'profile_type': profile_type,
        'function_name': func_name,
        'stats': stats_str
    }
    profiling_results.append(result_dict)

    print(f"Finished profiling.")
    return result_dict

def profile_function(profile_type="unoptimized"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            profiler = LineProfiler()
            profiler.add_function(func)
            result = profiler(func)(*args, **kwargs)

            stats_stream = StringIO()
            profiler.print_stats(stream=stats_stream)
            stats_str = stats_stream.getvalue()

            result_dict = save_profiling_result(profile_type, func.__name__, stats_str)
            return result, result_dict

        return wrapper
    return decorator

def get_mean_profile_times():
    hits_list = []
    time_list = []
    per_hit_list = []
    percent_time_list = []
    
    for result in profiling_results:
        stats_lines = result['stats'].split("\n")
        for line in stats_lines:
            parts = line.split()
            if len(parts) > 4 and parts[0].isdigit(): 
                try:
                    hits = int(parts[1])       
                    time = float(parts[2])    
                    per_hit = float(parts[3])
                    percent_time = float(parts[4])  
                    
                    hits_list.append(hits)
                    time_list.append(time)
                    per_hit_list.append(per_hit)
                    percent_time_list.append(percent_time)

                except ValueError:
                    pass  
  
    mean_hits = mean(hits_list) if hits_list else 0
    mean_time = mean(time_list) if time_list else 0
    mean_per_hit = mean(per_hit_list) if per_hit_list else 0
    mean_percent_time = mean(percent_time_list) if percent_time_list else 0


    mean_results = {
        "Mean Hits": mean_hits,
        "Mean Time": mean_time,
        "Mean Per Hit": mean_per_hit,
        "Mean % Time": mean_percent_time
    }
    
    print("Mean Profiling Results:")
    for key, value in mean_results.items():
        print(f"{key}: {value:.6f}")

    return mean_results
