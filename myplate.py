# Determines a recipe's value on the Myplate system
def myplate():
    veg_yn = input('Does meal contain servings of vegitables?')
    if veg_yn == 'yes':
        veg_s = input('How many?')
    elif veg_yn == 'no':
        veg_s = 0
    else:
        print('invalid input!')
    fruit_yn = input('Does meal contain servings of fruit?')
    if fruit_yn == 'yes':
        fruit_s = input('How Many?')
    elif fruit_yn == 'no':
        fruit_s = 0
    else:
        print('invalid input!')
    grains_yn = input('Does meal contain servings of grains?')
    if grains_yn == 'yes':
        grains_s = input('How Many?')
    elif grains_yn == 'no':
        grains_s = 0
    else:
        print('invalid input!')
    protien_yn = input('Does meal contain servings of protien?')
    if protien_yn == 'yes':
        protien_s = input('How Many?')
    elif protien_yn == 'no':
        protien_s = 0
    else:
        print('invalid input!')

    print('This meal contains:')
    print(veg_s,'serving(s) of vegitables')
    print(fruit_s,'serving(s) of fruit')
    print(grains_s,'serving(s) of grains')
    print(protien_s,'serving(s) of protien')

myplate()
