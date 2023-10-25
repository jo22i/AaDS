# Задача 1

def Fibbonachi(n):
    a0 = 1
    a1 = 1

    if(n == 0): return 0
    elif(n <= 2 and n > 0): return 1

    for i in range(3, n+1):
        a0, a1 = a1, a0
        a1 += a0
    return a1

#print(Fibbonachi(int(input())))

# Задача 5

# def a_search(a, n, mass):
#     row = n
#     column = n

#     if(mass[row][column] < a): return False

#     while True:
#         if(row == 1 or column == 1): return False
        
# Задача 7

def mass_answ(nums):
    answer = [1] * len(nums)
        
    for i in range(0, len(nums)):
        for j in range(0, len(answer)):
            if (j != i): answer[j] *= nums[i]

    return answer

# nums = [3, 7, 0, 6]
# print(mass_answ(nums))
