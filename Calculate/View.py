def InputData(number):
    number=int(input(f'Введите число {number}: '))
    return number

def OutputData(number):
    print(f' Число {number}')

def OutputResult(number):
    print(f'Результат операции = {number}')

def InputOperation():
    oper = input(f'Введите оператор: ')
    return oper

def division_by_zero():
    print('Деление на ноль!')