# Determine's a recipe's value on the Myplate system
def Myplate():
    veg_yn = input('Does meal contain servings of vegitables?')
    print(veg_yn)
    if veg_yn.lower == 'yes':
        veg_s = input('How many?')
        print(veg_s)
    fruit_yn = input('Does meal contain servings of fruit?')
    if fruit_yn.lower == 'yes':
        fruit_s = input('How Many?')
    grains_yn = input('Does meal contain servings of grains?')
    if grains_yn.lower == 'yes':
        grains_s = input('How Many?')
    protien_yn = input('Does meal contain servings of protien?')
    if protien_yn.lower == 'yes':
        protien_s = input('How Many?')
    

        
