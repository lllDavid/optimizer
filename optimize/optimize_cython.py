import os
import subprocess
import importlib.util
import sys
import inspect

def extract_function_code(file_path, func_name):
    try:
        with open(file_path, "r") as file:
            code = file.read()
        
        compiled = compile(code, file_path, 'exec')
        func_code = None
        
        exec(compiled, globals())
        
        if func_name in globals():
            func_code = inspect.getsource(globals()[func_name]).split("\n", 1)[1]
        
        return func_code
    except Exception as e:
        print(f"Error extracting function {func_name}: {e}")
        return None

def generate_cython_code(func_name, func_code, func_dir):
    os.makedirs(func_dir, exist_ok=True)  
    cython_file_path = os.path.join(func_dir, f"optimized_{func_name}.pyx")  
    
    cython_code = f"""
def {func_name}(A, B):
{func_code}
    """
    
    with open(cython_file_path, "w") as f:
        f.write(cython_code)
    return cython_file_path

def compile_cython_file(func_name, func_dir):
    setup_code = f"""
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("optimized_{func_name}.pyx", compiler_directives={{'language_level': "3"}}),
)
"""
    
    setup_path = os.path.join(func_dir, "setup.py")
    with open(setup_path, "w") as f:
        f.write(setup_code)
    
    try:
        subprocess.check_call([sys.executable, "setup.py", "build_ext", "--inplace"], cwd=func_dir)
        print(f"Compiled optimized_{func_name}.pyx into a Cython module in {func_dir}.")
    except subprocess.CalledProcessError as e:
        print(f"Error during compilation: {e}")

def load_compiled_function(func_name, func_dir):
    sys.path.append(func_dir)  
    try:
        module = importlib.import_module(f"optimized_{func_name}") 
        return getattr(module, func_name)
    except Exception as e:
        print(f"Error loading {func_name}: {e}")
        return None

def generate_run_file(func_name, func_dir):
    run_file_path = os.path.join(func_dir, "run.py")
    run_code = f"""
from functions.optimized.{func_name}.optimized_{func_name} import {func_name}
from benchmarks.time import time_function
from benchmarks.profiler import profile_function
from random import randint

@time_function(repetitions=10)
# TODO: find way to profile the actual some_func lines not the wrapper
@profile_function(profile_type="optimized")
def decorated_{func_name}(*args, **kwargs):
    return {func_name}(*args, **kwargs)

def main():
    size = 50
    min_val = 1
    max_val = 10
    A = [[randint(min_val, max_val) for _ in range(size)] for _ in range(size)]
    B = [[randint(min_val, max_val) for _ in range(size)] for _ in range(size)]

    decorated_{func_name}(A, B)

if __name__ == "__main__":
    main()
"""
    with open(run_file_path, "w") as f:
        f.write(run_code)
    print(f"Generated run.py in {func_dir}.")

def dynamic_cython(func_name, func_code):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../functions/optimized"))
    func_dir = os.path.join(base_dir, func_name)
    generate_cython_code(func_name, func_code, func_dir)
    compile_cython_file(func_name, func_dir)
    generate_run_file(func_name, func_dir)

def main():
    file_path = input("Enter the file path (optimize\\test_function.py): ")
    func_name = input("Enter the name of the function you want to cythonize (test_func): ")
    
    func_code = extract_function_code(file_path, func_name)
    
    if func_code is None:
        print(f"Could not extract the code for {func_name} from {file_path}.")
        return
    
    dynamic_cython(func_name, func_code)

if __name__ == "__main__":
    main()