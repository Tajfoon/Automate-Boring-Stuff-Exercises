import random, sys
# Task of this program is to type item name, and check it current status. For example if
# can of beverage stands firmly on table, dont do anything, otherwise do something to elimite damage.

def itemStands(item, status):

    while True:
        while True:
            if item == 'can' or item == 'botle':
                print(f"Choosen item is {item}")
                break

            else:
                print('Wrong item. Try to choose something else')
                continue

        if status == 0:
            print(f'{item} stands firmly.')
        else:
            print(f'{item} fall down!')
        break

itemStands('can', random.randint(0, 1))

