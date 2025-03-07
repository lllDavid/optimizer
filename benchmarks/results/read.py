import pstats
import os

def get_stats(file: str, directory: str):
    file_path = os.path.join(directory, file)
    if os.path.exists(file_path):
        loaded_stats = pstats.Stats(file_path)
        print(f"\n{directory.capitalize()} stats:")
        loaded_stats.sort_stats('cumulative')
        loaded_stats.print_stats()
    else:
        print(f"{directory.capitalize()} file '{file}' not found!")

file_name = str(input("Benchmarks to compare:"))

get_stats(file_name, "before")  
get_stats(file_name, "after")   
