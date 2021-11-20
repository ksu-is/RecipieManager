# Determines a recipe's value on the Myplate system
def myplate():
    veg_yn = input('Does meal contain servings of vegitables?')
    if veg_yn == 'yes':
        veg_s = input('How many cups?')
    elif veg_yn == 'no':
        veg_s = 0
    else:
        print('invalid input!')
    fruit_yn = input('Does meal contain servings of fruit?')
    if fruit_yn == 'yes':
        fruit_s = input('How Many cups?')
    elif fruit_yn == 'no':
        fruit_s = 0
    else:
        print('invalid input!')
    grains_yn = input('Does meal contain servings of grains?')
    if grains_yn == 'yes':
        grains_s = input('How Many ounces?')
    elif grains_yn == 'no':
        grains_s = 0
    else:
        print('invalid input!')
    protien_yn = input('Does meal contain servings of protien?')
    if protien_yn == 'yes':
        protien_s = input('How Many ounces?')
    elif protien_yn == 'no':
        protien_s = 0
    else:
        print('invalid input!')
    dairy_yn = input('Does meal contain servings of dairy?')
    if dairy_yn == 'yes':
        dairy_s = input('How Many cups?')
    elif dairy_yn == 'no':
        dairy_s = 0
    else:
        print('invalid input!')
    print('This meal contains:')
    print(veg_s,'cups(s) of vegitables,',float(veg_s)/2.5*100,'percent of the recomended daily amount.')
    print(fruit_s,'cups(s) of fruit,',int(fruit_s)/2*100,'percent of the recomended daily amount.')
    print(grains_s,'ounces(s) of grains,',int(grains_s)/6*100,'percent of the recomended daily amount.')
    print(protien_s,'ounces(s) of protien,',float(protien_s)/5.5*100,'percent of the recomended daily amount.')
    print(dairy_s,'cups of dairy,',int(dairy_s)/3*100,'percent of the recomeneded daily amount.')

myplate()
