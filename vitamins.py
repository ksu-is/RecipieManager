while True:
    age = input('Enter your age: ')
    gender = input('Enter your gender. Enter m for male and f for female: ')
    # for calcium
    cal = input('How much calcium does your recipe contain in mg?')
    if int(age) < 50:
        print("Your recipe contains",int(cal)/1000*100,'% of the recomended daily amount.')
    elif int(age) > 50 and gender == 'f' or int(age) > 70 and gender == 'm':
        print("Your recipe contains",int(cal)/1200*100,'% of the recomended daily amount.')
    
    # for vitamin a
    vita = input('How much vitamin a does your recipe contain in mcg?')
    if gender == 'm':
        print("Your recipe contains",int(vita)/900*100,'% of the recomended daily amount.')
    elif gender == 'f':
        print("Your recipe contains",int(vita)/700*100,'% of the recomended daily amount.')

    # for for vitamin c
    vitc = input('How much vitamin c does your recipe contain in mg?')
    if gender == 'm':
        print("Your recipe contains",int(vitc)/90*100,'% of the recomended daily amount.')
    elif gender == 'f':
        print("Your recipe contains",int(vitc)/75*100,'% of the recomended daily amount.')

    # for for vitamin d
    vitd = input('How much vitamin d does your recipe contain in mcg?')
    if int(age) < 71:
        print("Your recipe contains",int(vitd)/15*100,'% of the recomended daily amount.')
    else:
        print("Your recipe contains",int(vitd)/20*100,'% of the recomended daily amount.')

    # for for iron
    vitc = input('How much iron does your recipe contain in mg?')

    if gender == 'f' and age < 51:
        print("Your recipe contains",int(vitc)/18*100,'% of the recomended daily amount.')
    else:
        print("Your recipe contains",int(vitc)/8*100,'% of the recomended daily amount.')

    
    
    break
    
