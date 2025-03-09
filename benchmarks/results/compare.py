from os import path

def parse_lprof_output(lprof_text):
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

def compare(file: str, directory: str):
    file_path = path.join(directory, file)
    if path.exists(file_path):
        with open(file_path, 'r') as f:
            lprof_text = f.read()

        stats_dict = parse_lprof_output(lprof_text)

        return stats_dict
    else:
        print(f"{directory.capitalize()} file '{file}' not found!")
        return None


def display_comparison(before_stats, optimized_stats):
    print("Comparing Function Calls and Cumulative Time:")

    total_before_time = 0
    total_optimized_time = 0

    for line_num in before_stats:
        if line_num in optimized_stats:
            before_data = before_stats[line_num]
            optimized_data = optimized_stats[line_num]

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
            print(f"\nLine {line_num}: Function not found in 'optimized' stats.")

    if total_before_time > 0:
        performance_increase_percent = ((total_before_time - total_optimized_time) / total_before_time) * 100
        print(f"\nTotal Performance Increase: {performance_increase_percent:.2f}%")
    else:
        print("\nTotal performance increase: N/A (Before time is 0).")


file_name = str(input("Benchmarks to compare:"))

before_stats = compare(file_name, "before")
optimized_stats = compare(file_name, "optimized")

if before_stats and optimized_stats:
    display_comparison(before_stats, optimized_stats)
