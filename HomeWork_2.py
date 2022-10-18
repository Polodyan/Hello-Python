# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# float_num = input('input float number: ')
# # print(type(float_num))
# sum = 0
# for i in float_num:
#     if i != '.':
#         sum += int(i)
# print(sum)

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('input N: '))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
#     print(factorial, end=' ')

# 3. Задайте список из n чисел последовательности (1+1/n)^n
# Выведитте на экран саму последовательность и сумму элеементов этой последовательности (для проверки сумма для 4 элементов = 9,06 (примерно))

# n = int(input('Enter number: ')) 

# def sequence(n):

#     return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
# print(sequence(n))
# print(round(sum(sequence(n))))

# 4. Реализуйте алгоритм перемешивания списка, без использования встроеных методов (особенно SHUFFLE, без него) можно (нужно) использовать библиотеку Random

# import random
# lst = [random.randint(0,10) for i in range(random.randint(5,20))]
# print(f"исходный список:\n {lst}")
# random.shuffle(lst)
# print(f"список после перемешивания:\n{lst}")