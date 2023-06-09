# Задание №1

from pprint import pprint
import json

with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for cook_book_name in file:
        ingredient_count = int(file.readline())
        ingredient_list = []
        for i in range(ingredient_count):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            ingredient_list.append({'ingredient_name': ingredient_name,
                                    'quantity': quantity,
                                    'measure': measure})
        file.readline()
        cook_book[cook_book_name.strip()] = ingredient_list
    res = json.dumps(cook_book, ensure_ascii=False, indent=2)

print(f'cook_book = {res}')


# Задание №2

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredients in cook_book[dish]:
                if ingredients['ingredient_name'] not in shop_list:
                    value = {'quantity': int(ingredients['quantity']) * person_count, 'measure': ingredients['measure']}
                    shop_list[ingredients['ingredient_name']] = value
                else:
                    shop_list[ingredients['ingredient_name']]['quantity'] += int(ingredients['quantity']) * person_count

    return shop_list


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

# Задание №3 открытие и запись в один файл

import os


def final_file():
    os.chdir('2.4.files/sorted')
    with open('1.txt', 'r', encoding='UTF-8') as file1:
        f1 = file1.readlines()
    with open('2.txt', 'r', encoding='UTF-8') as file2:
        f2 = file2.readlines()
    with open('3.txt', 'r', encoding='UTF-8') as file3:
        f3 = file3.readlines()
    with open('1final_file.txt', 'w', encoding='UTF-8') as file_to_write:
        if len(f1) < len(f2) and len(f1) < len(f3):
            file_to_write.write('1.txt' + '\n')
            file_to_write.write(str(len(f1)) + '\n')
            file_to_write.writelines(f1)
            file_to_write.write('\n')
        elif len(f2) < len(f1) and len(f2) < len(f3):
            file_to_write.write('2.txt' + '\n')
            file_to_write.write(str(len(f2)) + '\n')
            file_to_write.writelines(f2)
            file_to_write.write('\n')
        elif len(f3) < len(f1) and len(f3) < len(f2):
            file_to_write.write('3.txt' + '\n')
            file_to_write.write(str(len(f3)) + '\n')
            file_to_write.writelines(f3)
            file_to_write.write('\n')
        if len(f2) > len(f1) > len(f3) or len(f2) < len(f1) < len(f3):
            file_to_write.write('1.txt' + '\n')
            file_to_write.write(str(len(f1)) + '\n')
            file_to_write.writelines(f1)
            file_to_write.write('\n')
        elif len(f1) > len(f2) > len(f3) or len(f2) > len(f1) and len(f2) < len(f3):
            file_to_write.write('2.txt' + '\n')
            file_to_write.write(str(len(f2)) + '\n')
            file_to_write.writelines(f2)
            file_to_write.write('\n')
        elif len(f1) > len(f3) > len(f2) or len(f3) > len(f1) and len(f3) < len(f2):
            file_to_write.write('3.txt' + '\n')
            file_to_write.write(str(len(f3)) + '\n')
            file_to_write.writelines(f3)
            file_to_write.write('\n')
        if len(f1) > len(f2) and len(f1) > len(f3):
            file_to_write.write('1.txt' + '\n')
            file_to_write.write(str(len('1.txt')) + '\n')
            file_to_write.writelines('1.txt')
        elif len(f2) > len('1.txt') and len(f2) > len(f3):
            file_to_write.write('2.txt' + '\n')
            file_to_write.write(str(len(f2)) + '\n')
            file_to_write.writelines(f2)
        elif len(f3) > len('1.txt') and len(f3) > len(f2):
            file_to_write.write('3.txt' + '\n')
            file_to_write.write(str(len(f3)) + '\n')
            file_to_write.writelines(f3)

    return final_file


print(final_file())
