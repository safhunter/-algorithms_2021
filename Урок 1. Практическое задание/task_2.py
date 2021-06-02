"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.

Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""

import random


# Сложность O(n^2)
def find_min_1(num_list):
    if len(num_list) == 0:                                              # O(1)
        return None                                                     # O(1)
    elif len(num_list) == 1:                                            # O(1)
        return num_list[0]                                              # O(1)

    for i in range(len(num_list)):                                      # O(n)
        for j in range(i+1, len(num_list)):                             # O(n)
            if num_list[i] > num_list[j]:                               # O(1)
                break                                                   # O(1)
        if (j == len(num_list)-1) and (num_list[i] <= num_list[j]):     # O(1)
            return num_list[i]                                          # O(1)


# Сложность O(n)
def find_min_2(num_list):
    if len(num_list) == 0:                                              # O(1)
        return None                                                     # O(1)

    min_elem = num_list[0]                                              # O(1)
    for elem in num_list:                                               # O(n)
        if elem < min_elem:                                             # O(1)
            min_elem = elem                                             # O(1)
    return min_elem                                                     # O(1)


lst = random.sample(range(-100000, 100000), 10)


print(lst)
print(find_min_1(lst))
print(find_min_2(lst))
