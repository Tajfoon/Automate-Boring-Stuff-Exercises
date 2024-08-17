import pprint, random, os, sys


# Check len of string and for every each char generate frame element

#FUNCTIONS --------------

def print_menu(lenof):
    menu_shape = ''
    lenof_string = str(lenof)
    for x in range(len(lenof_string)):
        menu_shape += '-'
    print(menu_shape)

    #Create function which is responsible for add items from table to dictionary.


# We have inventory[choosenCharacter].
# We want to modify inventory[choosenCharacter] when we defeat a monster and pick up an item

def addLoot(inv, monster_loot):
    loot_to_add = {}
    for x in monster_loot:
        if x in inv.keys():
            losowa_wartosc = random.randint(1, 6)
            loot_to_add[x] = losowa_wartosc
            print(f"{x}: {losowa_wartosc}", end=', ')
    pick_loot = input("Do you want to pick items?")
    if pick_loot == 'y':
        for k, v in loot_to_add.items():
            inv[k] += v
    print()



loot_items = ['gold_coins', 'rock']


inventory = {'Sam':{'health_potion':4,'gold_coins':300,'sticks':5,'rock':8},
             'Dragho':{'health_potion':4,'gold_coins':300,'sticks':5,'rock':8}}

while True:
    while True:
        print('Which player you wanna choose? If you want to exit press enter.')
        for player in inventory.keys():
            print(player)
        character_choose = str(input(''))

        if character_choose == '':
            sys.exit()
        elif character_choose in inventory:
            break
        else:
            print('Wrong character name, please try again')
            continue

    break


#After character choose print menu frame, nickname and equipment.


# print(len(str(inventory[character_choose])))
print(f'Name: {character_choose}')
print()
print(f'Inventory:')
print_menu(inventory[character_choose])
print(f"{inventory[character_choose]}")
print('Linia poniżej')
addLoot(inventory[character_choose], loot_items)
print(f"{inventory[character_choose]}")

#
print_menu(inventory[character_choose])

#Function which make table splitted by every each 2 characters of word.
#It's needed because above i create string maked concatenation with index of for loop and elements from table coords.
def split_every_two_characters(s):
    return [s[i:i+2] for i in range(0, len(s), 2)]

coords = ['a', 'b', 'c', 'd', 'e', 'f']

def mapGenerator(w, h):
    #for every each row reset dictionary and created map to start from beggining
    for heigh in range(h):
        map_gen = {}
        map = ''

        # to map string on every width add width index + heigh( which is index of row )
        for width in range(w):
            map += f'{width}{coords[heigh]}'

        splitted = split_every_two_characters(map)
        # print(splitted)
        for x in splitted:
            monster = random.randint(1, 3)
            #Set default which set empty area or danger area with moster depended on random monster spawn rate.
            if monster != 3:
                map_gen.setdefault(x, ' ')
            else:
                map_gen.setdefault(x, 'M')
        print(map_gen)

mapGenerator(10, 3)

# Next one - put your warrior on the map, and make him walk around the map. If he step on
# this same area where monster prepare fight. After won fight, warrior will get random generatd equpiment from
# monster. If warrior die, then start from beggining.