# Последовательность Фибоначи называеться последовательность чисел а0, а1, ..., an, ..., где 

# # a0 = 0, a1 = 1, ak - 1 + ak - 2 (k > 1).

# # 0, 1, 1, 2, 3, 5, 8, 13, 21 ...
# # Требуеться найти N-е число Фибоначи

# Var1
# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n-1) + fib(n-2)

# print(fib(6))

#Var2
# def fib_better(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     first = 0
#     second = 1
#     third = first + second
#     count = 2
#     while count < n:
#         first = second
#         second = third
#         third = first + second
#         count += 1
#     return third
    
# print(fib_better(6))


# Задача 33
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои 
# минимальные оценки на максимальные. Напишите программу, 
# которая заменяет оценки Василия, но наоборот: 
# все максимальные – на минимальные.

# Input: 5 -> 1 3 3 3 4 
# Output: 1 3 3 3 1

# Var_1
# n = int(input('Введите кол-во оценок: '))
# list_1 = []
# for _ in range(n):
#     list_1.append(int(input('Введите оценки: ')))
# print(list_1)
# max = 0
# for i in list_1:
#     if i > max:
#         max = i
# print(max)
# min = max
# for i in list_1:
#     if i < min:
#         min = i
# print(min)
# for i in range(len(list_1)):
#     if list_1[i] == max:
#         list_1[i] = min
# print(list_1)

# Var_2

# n = int(input('Введите кол-во оценок: '))
# list_1 = []
# for _ in range(n):
#     list_1.append(int(input('Введите оценки: ')))
# print(list_1)
# max = list_1[0]
# min = list_1[0]
# for i in range(1, len(list_1)):
#     if list_1[i] > max:
#         max = list_1[i]
#     if list_1[i] < min:
#             min = list_1[i]
# print(max, min)
# for i in range(len(list_1)):
#     if list_1[i] == max:
#         list_1[i] = min
# print(list_1)      



