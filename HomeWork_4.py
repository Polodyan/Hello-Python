# 1. Вычислить число ПИ c заданной точностью *d*

# import math
# from math import pi

# n = pi
# print(n)

# n = 100
# my_pi = sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) for x in range(n))

# print(my_pi)

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# num = int(input("Введите число: "))
# i = 2 # первое простое число
# lst = []
# old = num
# while i <= num:
#    if num % i == 0:
#        lst.append(i)
#        num //= i
#        i = 2
#    else:
#        i += 1
# print(f"Простые множители числа {old} приведены в списке: {lst}")

# 3. Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# num = int(input("Введите число: "))
# i = 2 # первое простое число
# lst = []
# old = num
# while i <= num:
#   if num % i == 0:
#        lst.append(i)
#        num //= i
#        i = 2
#    else:
#        i += 1
# print(f"Простые множители числа {old} приведены в списке: {lst}")

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k 
# k - максимальная степень многочлена, следующий степень на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

# import random


# def write_file(st):
#    with open('file33.txt', 'w') as data:
#        data.write(st)


#def rnd():
#    return random.randint(0,101)


#def create_mn(k):
#    lst = [rnd() for i in range(k+1)]
#    return lst
    

# def create_str(sp):
#    lst= sp[::-1]
#    wr = ''
#    if len(lst) < 1:
#        wr = 'x = 0'
#    else:
#        for i in range(len(lst)):
#            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                wr += f'{lst[i]}x^{len(lst)-i-1}'
#                if lst[i+1] != 0:
#                    wr += ' + '
#            elif i == len(lst) - 2 and lst[i] != 0:
#                wr += f'{lst[i]}x'
#                if lst[i+1] != 0:
#                    wr += ' + '
#            elif i == len(lst) - 1 and lst[i] != 0:
#                wr += f'{lst[i]} = 0'
#            elif i == len(lst) - 1 and lst[i] == 0:
#                wr += ' = 0'
#    return wr

# k = int(input("Введите натуральную степень k = "))
# koef = create_mn(k)
# write_file(create_str(koef))

# 5. Даны два файла, в каждом из которых находится запись многочлена.
#Задача - сформировать файл, содержащий сумму многочленов.

# with open('poly_1.txt', 'w', encoding='utf-8') as file:
#    file.write('2*x^2 + 5*x^5')
#with open('poly_2.txt', 'w', encoding='utf-8') as file:
#    file.write('23*x^4 + 9*x^6')

#with open('poly_1.txt','r') as file:
#    poly_1 = file.readline()
#    list_of_poly_1 = poly_1.split()


#with open('poly_2.txt','r') as file:
#    poly_2 = file.readline()
#    list_of_poly_2 = poly_2.split()

#print(f'{list_of_poly_1} + {list_of_poly_2}')
#sum_poly = list_of_poly_1 + list_of_poly_2

#with open('sum_poly.txt', 'w', encoding='utf-8') as file:
#    file.write(f'{list_of_poly_1} + {list_of_poly_2}')