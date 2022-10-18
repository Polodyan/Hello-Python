# Задание 1
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# my_list = [2, 3, 5, 9, 3]
# print(sum(my_list[1::2]))

# Задание 2
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# my_list = [2, 3, 4, 5, 6]
# result_list = []
# for i in range((len(my_list)+1)//2):
#     result_list.append(my_list[i]*my_list[len(my_list)-1-i])
# print(result_list)

# Задание 3
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов. Если число целое, то его дробная часть не считается за 0 и оно (число) в сравнении не участвует

# my_list = [1.1, 1.2, 3.1, 5, 10.01]
# min = 1
# max = 0
# for i in my_list:
#    if (i - int(i)) <= min:
#        min = i - int(i)
#    if (i - int(i)) >= max:
#        max = i - int(i)  
# print(max-min)

# Задание 4
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# s = ""
# n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
# while n != 0:
#    s = str(n%2) + s
#    n //=2
# print(s)

# Задание 5
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите число: '))

def get_fibonacci(n):
    fibo_nums = []
    a, b = 1, 1
    for i in range(n-1):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    return fibo_nums

fibo_nums = get_fibonacci(n)
print(get_fibonacci(n))
print(fibo_nums.index(0))