# Determine's a recipe's value on the Myplate system
def myplate():
    veg_yn = input('Does meal contain servings of vegitables?')
    print(veg_yn)
    if veg_yn == 'yes':
        veg_s = input('How many?')
        print(veg_s)
    else:
        print('No vegitable servings')
    fruit_yn = input('Does meal contain servings of fruit?')
    if fruit_yn == 'yes':
        fruit_s = input('How Many?')
    grains_yn = input('Does meal contain servings of grains?')
    if grains_yn == 'yes':
        grains_s = input('How Many?')
    protien_yn = input('Does meal contain servings of protien?')
    if protien_yn == 'yes':
        protien_s = input('How Many?')


myplate()

        
