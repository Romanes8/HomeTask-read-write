cook_book = {}

with open('recipes.txt', encoding = 'utf-8') as f:
    for dish in f:
        dish = dish[0:-1]
        count = int(f.readline())
        list_ingredients = []
        for i in range(count):
            ingredient = f.readline().split(' | ')
            list_ingredients.append({'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2][0:-1]})
        cook_book[dish]=list_ingredients
        f.readline()
    print(cook_book)










