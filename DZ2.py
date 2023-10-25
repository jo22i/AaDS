# Задача 2

line = str(input())

max_count = 0
count = 0
tick = 0

for i in range(0, len(line)):
    if(line[i] == '('):
        count += 1
        tick += 1
    elif(line[i] == ')'):
        count -= 1
        tick += 1

    if(count < 0):
        count, tick = 0, 0
    elif(count == 0 and tick > max_count):
        max_count = tick
        tick = 0 

print(max_count)   