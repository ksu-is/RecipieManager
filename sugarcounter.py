# for sodium
# Determined by the Institute of Medicine
age = input('Enter your age: ')
gender = input('Enter your gender. Enter m for male and f for female: ')
sodium = input('How much sodium does your recipe contain in mg?')

if int(age) < 50:
    print("Your recipe contains",int(sodium)/1500*100,'% of the recomended daily amount.')
elif int(age) > 50 and int(age) < 71:
    print("Your recipe contains",int(sodium)/1300*100,'% of the recomended daily amount.')
elif int(age) > 71:
    print("Your recipe contains",int(sodium)/1200*100,'% of the recomended daily amount.')

# for Saturated Fat
# Calorie count information from U.S. Department of Health and Human Services
# Daily % determined by the American Heart Association

sf = input('How much calories of saturated fat does your recipe contain?')

if gender == 'm':
    print("Your recipe contains",int(sf)/125*100,'% of the recomended daily amount.')
elif gender == 'f':
    print("Your recipe contains",int(sf)/100*100,'% of the recomended daily amount.')

# For added sugar
# Determined by U.S. Department of Health and Human Services
sugar = input('How many teaspoons of added sugar does your recipe contain?')

print("Your recipe contains",int(sugar)/12*100,'% of the recomended daily amount.')
