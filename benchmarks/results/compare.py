from os import path

def parse_lprof_text(lprof_text):
    parsed_data = {}

    lines = lprof_text.splitlines()

    data_start_index = None
    for idx, line in enumerate(lines):
        if line.strip().startswith("Line #"): 
            data_start_index = idx
            break

    if data_start_index is not None:
        for line in lines[data_start_index + 1:]:  
            columns = line.split()

            if len(columns) < 6 or columns[0].lower() == "line":
                continue

            try:
                line_num = int(columns[0])  
                hits = int(columns[1])  
                total_time = float(columns[2]) 
                per_hit_time = float(columns[3])  
                percent_time = float(columns[4]) 
                line_contents = " ".join(columns[5:])  

                parsed_data[line_num] = {
                    'hits': hits,
                    'time': total_time,
                    'per_hit_time': per_hit_time,
                    'percent_time': percent_time,
                    'line_contents': line_contents
                }
            except ValueError:
                continue

    return parsed_data

def load_lprof_file(file: str, directory: str):
    file_path = path.join(directory, file)
    if path.exists(file_path):
        with open(file_path, 'r') as f:
            lprof_text = f.read()

        stats_dict = parse_lprof_text(lprof_text)

        return stats_dict
    else:
        print(f"{directory.capitalize()} file '{file}' not found!")
        return None


def compare(file_name):
    print("Comparing Function Calls and Cumulative Time:")

    before_stats = load_lprof_file(file_name, "benchmarks/results/before")
    optimized_stats = load_lprof_file(file_name, "benchmarks/results/optimized")

    if not before_stats or not optimized_stats:
        print("Error: One or both of the stats files are missing.")
        return

    total_before_time = 0
    total_optimized_time = 0

    all_line_nums = set(before_stats.keys()).union(optimized_stats.keys())

    for line_num in all_line_nums:
        before_data = before_stats.get(line_num)
        optimized_data = optimized_stats.get(line_num)

        if before_data and optimized_data:
            before_hits = before_data['hits']
            optimized_hits = optimized_data['hits']
            before_time = before_data['time']
            optimized_time = optimized_data['time']
            before_percent_time = before_data['percent_time']
            optimized_percent_time = optimized_data['percent_time']

            print(f"\nLine {line_num}: {before_data['line_contents']}")
            print(f"  Before Hits: {before_hits}, Optimized Hits: {optimized_hits}")
            print(f"  Before Total Time: {before_time:.6f}s, Optimized Total Time: {optimized_time:.6f}s")
            print(f"  Before % Time: {before_percent_time:.2f}%, Optimized % Time: {optimized_percent_time:.2f}%")
            time_change = optimized_time - before_time
            print(f"  Time Change: {time_change:.6f}s")

            total_before_time += before_time
            total_optimized_time += optimized_time
        else:
            if before_data:
                print(f"\nLine {line_num}: Present only in 'before' stats.")
            if optimized_data:
                print(f"\nLine {line_num}: Present only in 'optimized' stats.")

    if total_before_time > 0:
        performance_increase_percent = ((total_before_time - total_optimized_time) / total_before_time) * 100
        print(f"\nTotal Performance Increase: {performance_increase_percent:.2f}%")
    else:
        print("\nTotal performance increase: N/A (Before time is 0).")


