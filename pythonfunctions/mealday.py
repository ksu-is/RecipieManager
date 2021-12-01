#Enter favorite meal to have according to time of day
meal_day = input('What is your favorite time of the day to eat a meal? Enter m for morning and l for middle and d for night')
if meal_day == 'm':
    meal_day_s = input('Then you will love our breakfast recipes! ')
elif meal_day == 'l':
    meal_day_s = input('Then you will love our lunch recipes!')
elif meal_day == 'd':
    meal_day_s = input('Then you will love our dinner recipes! ')
else:
    print('Invalid input!')
