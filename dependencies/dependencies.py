import sys
import subprocess
import importlib.util

dependencies = []

def install_module(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def insert_dependencies(dependencies_list, logEnabled):
    if logEnabled == True:
        for i in dependencies_list:
            print(i)
            dependencies.append(i)
    else:
        for i in dependencies_list:
            dependencies.append(i)
    
def check_for_module(name):
    if name in sys.modules:
        print(f"{name!r} already in sys.modules")
    elif (spec := importlib.util.find_spec(name)) is not None:
        install_module(name)
        print(f"{name!r} has been imported")
    else:
        print(f"can't find the {name!r} module")

def install_dependencies():
    try:
        for i in dependencies:
            check_for_module(i)
    except Exception as e:
        print(f"Exeption caught {e}")
