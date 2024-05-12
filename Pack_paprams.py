def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print("1.  ФУНКЦИЯ С ПАРАМЕТРАМИ ПО УМОЛЧАНИЮ")
print()
print('Вызов функции без аргументов:')
print_params()
print('------------------------')
print('Изменен параметр b:')
print_params(b = 25)
print('------------------------')
print(("Изменен параметр c:"))
print_params(c = [1, 2, 3])
print('*****************************************')

print('2. РАСПАКОВКА ПАРАМЕТРОВ')
value_list =[555, 'Привет', True]
value_dict = {'a': 51, 'b': "Пока", 'c': False}
print_params(*value_list)
print_params(**value_dict)
print('******************************************')

print('РАСПАКОВКА + ОТДЕЛЬНЫЕ ПАРАМЕТРЫ')
values_list_2 = [777, 'Hello']
print_params(*values_list_2, 42)