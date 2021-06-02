"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""


class Company(object):

    def __init__(self, name: str, profit: float):
        if name == '':
            raise ValueError('Company name cant be empty')
        self.name = name
        self.profit = profit

    def __lt__(self, other):
        return self.profit < other.profit

    def __le__(self, other):
        return self.profit <= other.profit

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'({self.name}: {self.profit})'


"""
    Сложность: O(n*logn)
    Сложность обусловлена применением метода sorted()
"""


def find_best_1(companies_list):
    if len(companies_list) == 0:
        return None
    elif len(companies_list) < 4:
        return companies_list

    return sorted(companies_list, reverse=True)[:3]


"""
    Сложность: O(n)
    Сложность обусловлена последовательным применением методов list.index (сложность O(n)) и max(list) (сложность O(n))
    соотвественно общая сложность без учета константого O(1): 2*O(n), константый множитель можно не учитывать
    в итоге получается O(n) 
"""


def find_best_2(companies_list):
    if len(companies_list) == 0:
        return None
    elif len(companies_list) < 4:
        return companies_list

    result_list = []
    for i in range(3):
        result_list.append(companies_list.pop(companies_list.index(max(companies_list))))
    return result_list


"""
    Сложность: O(n)
    Немножко модернизированный вариант функции find_best_2(), имеет ту же сложность O(n), но выполняется чуть
    быстрее за счет отсутствия константного множителя 2. От него удалось избавиться, заменив последовательный вызов
    max(list), list.index() на функцию find_max_index() которая сразу возвращает индех максимального элемента в списке.
    В итоге этот способ получается наиболее эффективным из представленных. 
"""


def find_max_index(source_list):
    max_elem = source_list[0]  # O(1)
    max_idx = 0
    for i, elem in enumerate(source_list):  # O(n)
        if elem > max_elem:  # O(1)
            max_elem = elem  # O(1)
            max_idx = i
    return max_idx


def find_best_3(companies_list):
    if len(companies_list) == 0:
        return None
    elif len(companies_list) < 4:
        return companies_list

    result_list = []
    for i in range(3):
        result_list.append(companies_list.pop(find_max_index(companies_list)))
    return result_list


lst = [Company(x, y) for x, y in (('1', 100), ('2', 300), ('3', 41), ('4', 500), ('5', 10))]

# print(str(lst))
print(find_best_1(lst.copy()))
print(find_best_2(lst.copy()))
print(find_best_3(lst.copy()))
