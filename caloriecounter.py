# Calorie counter
while True:
    gender = input('Enter your gender. Enter m for male and f for female: ')

    calories = input('Enter the amount of calories your meal contains: ')

    if gender == 'm':
        print('Your meal contains',calories, 'calories, or',int(calories)/2500*100,'percent of the recomended daily amount.')

    elif gender == 'f':
        print('Your meal contains',calories, 'calories, or',int(calories)/2000*100,'percent of the recomended daily amount.')
    elif gender == 'q':
        break
    else:
        print('Invalid input!')
