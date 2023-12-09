import sys
from collections import defaultdict

def SearchPaths(dep_lib: str, current_path: list):
    current_path = [dep_lib] + current_path 
    if dep_lib in dependencies:
        print(' '.join(current_path))

    if dep_lib in libs:
        for lib in libs[dep_lib]:
            if lib not in current_path:
                SearchPaths(lib, current_path)


vulnerables = set(input().split())
dependencies = set(input().split())

libs = defaultdict(set)

for line in sys.stdin:
    line = line.strip('\n')
    if line:
        lib_name, *lib_depends = line.split()
        
        for elem in lib_depends:
            libs[elem].add(lib_name)

for elem in vulnerables:
    SearchPaths(elem, [])