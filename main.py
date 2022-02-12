from pprint import pprint
import os

def get_list_for_cook_book():
    with open('recipes.txt', 'r', encoding='utf-8') as f:
        cook_book = dict()
        for iter in f:
            food_name = iter.strip('\n')
            count = int(f.readline().strip('\n'))
            food_list = []
            for i in range(count):
                name, sht, lt = f.readline().strip().split(' | ')
                food_list.append({'ingredient_name':name, 'quantity':sht, 'measure':lt})
            cook_book[food_name] = food_list
            f.readline()
        return cook_book


def get_shop_list_by_dishes(dishes = [], person_count = 1):
    recip_book = get_list_for_cook_book()
    ingredient_dict = {}
    for dish in dishes:
        for food in recip_book:
            ingredient = ''
            if dish == food:
                ingredient = recip_book.get(dish)
                for ingr in ingredient:
                    name = ingr['ingredient_name']
                    quantity, measure = int(ingr['quantity']), ingr['measure']
                    if name in ingredient_dict:
                        i = ingredient_dict[name]['quantity']+quantity*2
                        ingredient_dict[name] = {"measure": measure, 'quantity': i}
                    else:
                        ingredient_dict[name] = {"measure": measure, 'quantity': quantity * person_count}
    return ingredient_dict

def get_count_line_in_file(file):
    count_lines = 0
    with open(file, 'r', encoding='UTF-8') as f:
        for lines in f:
            count_lines += 1
    return count_lines


def generate_data_dict(files_dir):
    data = {}
    file_list = []
    for files in os.listdir(files_dir):
        if files.endswith(".txt"):
            file_list.append(files)
    for file in file_list:
        path_file = os.path.join(files_dir, file)
        with open(path_file, 'r', encoding='UTF-8') as f:
            file_name = os.path.basename(path_file)
            properties = (get_count_line_in_file(path_file), f.read().strip())
            data[file_name] = properties
    return data


def sort_write_data_dict(data):
    sorted_list = sorted(data.items(), key=lambda item: item[1][0])
    sorted_dict = {k: v for k, v in sorted_list}
    with open(os.path.join('result_file', 'result.txt'), 'w', encoding='UTF-8') as f:
        for k, v in sorted_dict.items():
            f.write(k + '\n')
            f.write(str(v[0]) + '\n')
            f.write(v[1] + '\n')
    return

sort_write_data_dict(generate_data_dict('files'))

pprint(get_list_for_cook_book())
pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))
sort_write_data_dict(generate_data_dict('files'))



























    
