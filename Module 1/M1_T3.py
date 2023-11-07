import sys

def SearchPaths(dep_lib: str):
    global libs, vulnerables

    path = list()
    
    pass


vulnerables = list(input().strip().split())
dependencies = list(input().strip().split())

libs = dict(set())

for line in sys.stdin:
    line = line.strip('\n')
    if (line == "" or line.find(" ") == 0): continue

    lib_name, *lib_depends = line.split()
    
    for elem in lib_depends:
        if libs.get(elem) is None:
            libs[elem] = set(lib_name)
        else:
            libs[elem].add(lib_name)

for elem in dependencies:
    SearchPaths(elem)