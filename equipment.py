# Add cooking equipment to the list

equipment = []
while True:
    enter_equip = input('Enter the cooking equipment you have availible: ')
    equipment.append(enter_equip)

    print(equipment)

    if enter_equip == 'q':
        break
# continue editing to add list to .txt file
