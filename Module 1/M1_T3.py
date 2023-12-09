import sys

def SearchPaths(item, lib_path, libs_visited, grath, libs_printed):
    global dependencies

    if item not in libs_visited:
        lib_path.append(item)
        libs_visited.add(item)

        if item in grath:
            for next_item in grath[item]:
                SearchPaths(next_item, lib_path, libs_visited, grath, libs_printed)

        if item in dependencies and tuple(lib_path) not in libs_printed:
            print(" ".join(reversed(lib_path)))
            libs_printed.add(tuple(lib_path))

        if lib_path:
            libs_visited.remove(item)
            lib_path.pop()


vulnerables = set(input().split())
dependencies = set(input().split())
lib_way = []
libs = {}

for line in sys.stdin:
    line = line.strip('\n')
    if line:
        lib_name, *lib_depends = line.split()
        
        for elem in lib_depends:
            libs.setdefault(elem, []).append(lib_name)

printed_paths = set()
for elem in vulnerables:
    SearchPaths(elem, lib_way, set(), libs, printed_paths)