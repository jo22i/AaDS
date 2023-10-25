vulnerables = []
dependencies = []
libs = dict()

vulnerables.extend(input().strip().split(" "))
dependencies.extend(input().strip().split(" "))

while(True):
    try:
        line = input().strip().split(" ", 1)
        lib_name, lib_dependencies = line[0], line[1].split(" ")
        libs[lib_name] = lib_dependencies

    except EOFError:
        # break
        for i in range(len(dependencies)):
            if (dependencies[i] in vulnerables):
                print(dependencies[i])

# Do smth for finding dependecies

