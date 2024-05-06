from pprint import pprint
from task1 import cook_book

dishes = ['Запеченный картофель','Омлет']

def get_shop_list_by_dishes(dishes, person_count):
    dict_ingredients = {}
    for dish in dishes:
        if dish in cook_book:
           for ingredients in cook_book[dish]:
               dict_ingredients[ingredients['ingredient_name']] = {'measure': ingredients['measure'], 'quantity': ingredients['quantity']*person_count}
        else:
           print(f'Блюдо {dish} отсутствует в кулинарной книге.')
    return dict_ingredients


pprint(get_shop_list_by_dishes(dishes, 2))










