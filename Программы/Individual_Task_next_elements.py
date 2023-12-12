#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант по списку - №31. Взят вариант №5. Первый вариант выполнения - элементы после пары.
if __name__ == '__main__':
    # Ввести кортеж одной строкой. Не обязательно должны быть только числа, поэтому map не нужен.
    A = tuple(input(
        "Good day! Please, enter elements.\nDon't forget putting spaces between them - ").split())
    # Введение переменных для проверки найденного элемента.
    first_pair_found = False
    previous_element = " "
    for i in A:
        if first_pair_found:
            print(i, end=" ")
        elif i == previous_element:
            print("Great news! We found a pair of equal elements -",
                  previous_element, "! List of next elements:")
            first_pair_found = True
        else:
            previous_element = i
    if not first_pair_found:
        print("Excuse us, but we couldn't find any pairs of equal elements.")
