ing_list = [] 
price_list = []
while True:
    ing = input("Enter your ingredients to the List: ")
    if ing == 'q':
        break
    price = float(input("Enter the price of the ingredient: "))
    ing_list.append(ing)
    price_list.append(price)
    print(ing_list)
    print(price_list)

print("Ingredient list:")
print('full list of ingredients',ing_list)
total_cost = sum(price_list)

print('Total cost of meal: ',total_cost)
