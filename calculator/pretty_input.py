

def pretty_input():
    from prettytable import PrettyTable  # pip install PrettyTable        
    import colorama as cs  # pip install colorama
    cs.init()
    print()
    print(cs.Fore.BLACK + '                                 КАЛЬКУЛЯТОР')
    print(cs.Fore.BLACK + '             для работы с рациональными и комплексными числами \n')
    print(cs.Style.BRIGHT, end='')
    print(cs.Fore.RED + '                            Инструкция пользователя\n')
    print(cs.Fore.BLUE + '          Арифметические действия и простые дроби обозначаются:')
    print(cs.Style.BRIGHT, end='')

    name = ['Сложение','Вычитание','Умножение','Деление','Дробь','Возведение в степень']
    data = ['+','-','*',':','/','^']

    columns = len(name)  
    table = PrettyTable(name)  
    data_data = data[:]     

    while data_data:    
        table.add_row(data_data[:columns])
        data_data = data_data[columns:]
    print(cs.Fore.BLUE, end='')
    print(table)
    print()

    name1 = ['Пример записи дроби с целой частью','Пример записи мнимой части','Пример степени']
    data1 = ['4_1/47','1_2/3:i, 1_2/3i , 1:i, 1:4i*i','Степень пишется одним целым числом: 5i^2*3 !=5i^6, =15i^2']

    columns1 = len(name1)  
    table1 = PrettyTable(name1)  
    data1_data1 = data1[:]     

    while data1_data1:    
        table1.add_row(data1_data1[:columns1])
        data1_data1 = data1_data1[columns1:]

    print(cs.Fore.BLUE,table1, end='\n')
    print()
    print(cs.Fore.RED + '                       Нереализованные(пока?) операции в калькуляторе')
    name2 = ['Логарифмы','Корень из числа','Раскрытие скобок','Возведение в степень(в процессе доработки)']
    table2 = PrettyTable(name2)
    table2.add_row(["log","√ ,sqrt",'1/(3+5), (2+3)*2','^'])
    print(table2)
    print(cs.Fore.GREEN)
    print("Для завершения работы введите пустую строку (просто Enter при пустом вводе)\n")
    cs.Style.RESET_ALL


pretty_input()

# cs.Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# cs.Style: DIM, NORMAL, BRIGHT, RESET_ALL

# colorama.init() # обязательно для Windows 10.
# print(cs.Fore.BLACK + 'Черный текст яркий')
# print(cs.Style.BRIGHT)
# print(cs.Fore.RED + 'Красный текст')
# print(cs.Fore.GREEN + 'Зеленый цвет')
# print(cs.Fore.BLUE + 'Синий цвет')
# print(cs.Fore.MAGENTA + 'Пурпурный цвет')
# print(cs.Fore.CYAN + 'Цвет морской волны')
# print(cs.Fore.RESET)
# print(cs.Style.RESET_ALL) # это сброс цветов консоли к начальным значениям.