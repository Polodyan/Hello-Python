# print('hello world')
# Тип данных и Переменные
# int, float, boolean, str, list, None
# value = None
# a = 123
# b = 1.23
# print(type(a))  # type для того, чтобы узнать тип данных
# print(type(b))
# value = 12334
# print(type(value))
# s = 'hello world'
# s = 'hello "world"'

# print(s) #вывод строки
# print(a, b, s)
# print(a, '-',b, '-', s)
# print('{} - {} - {}'.format(a,b,s))
# print(f'{a} - {b} - {s}')
# print('{1} - {2} - {0}'.format(a,b,s))

# f = True or False
# print(f)

# list = [] #массив
# list = ['1', '2', '3'] 
# col = ['hello', 1,2,4.5,True]
# print(list)
# print(col)

# Ввод и вывод данных
# print, input

# print('Введите a')
# a = int(input()) #если нужно целое число, используем функцию int
# print('Введите b')
# b = int(input())
# print(a, ' + ', b, ' = ', a+b)
# print('{} {}'.formate(a,b))
# print(f'{a} {b}')

# print('Введите a')
# a = float(input()) #если нужно вещественное число, используем функцию int
# print('Введите b')
# b = float(input())
# print(a, ' + ', b, ' = ', a+b)

# Арифметические операции
# +, -, *, /, %, //, **
# **, 
# (), Сокращенные операции

# a = 1.3
# b = 3
# c=round(a * b,3)
# print(c)

# a = 3
# a +=5
# print(a)

#Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# Кое-что еще: is, is not, in, not in

#f = [1,2,3,4]
# is_odd = not f[0] % 2
# print(is_odd)

#Управляющие конструкции
# if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#    print(a)
#else:
#    print(b)

#Управляющая конструкция while

# original = 23
# inverted = 0
# while original !=0:
  #  inverted = inverted * 10 + (original % 10)
    # original //= 10
#else:
 #   print('Пожалуй')
  #  print('хватит')
#print(inverted)

# list = [1,2,3,4,10,5]
# for i in list:
 #   print(i)

r = range(10)
for i in r:
    print(i)