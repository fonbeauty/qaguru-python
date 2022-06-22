# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и ее аргументов.
# Вызовите ее для трех функций ниже в цикле
# Подсказка: Имя функции можно получить с помощью func.__name__


def open_browser(arg1: str, arg2: int, arg3: bool):
    print(arg1, arg2, arg3)
    pass


def go_to_companyname_homepage(a: float, b: dict, c: list):
    print(a, b, c)
    pass


def find_registration_button_on_login_page(tup: tuple, sett: set, rang: range):
    print(tup, sett, rang)
    pass


def print_function(function):
    func_name = function.__name__.replace("_", " ")
    print(f'Функция "{func_name}" принимает аргументы:')
    for key, item in (function.__annotations__.items()):
        print(f'{key}: тип {item}')
    print()


func_list = [open_browser, go_to_companyname_homepage, find_registration_button_on_login_page]

for element in func_list:
    print_function(element)


