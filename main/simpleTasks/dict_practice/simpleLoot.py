import pprint, random, os, sys



def print_menu(lenof):
    menu_shape = ''
    lenof_string = str(lenof)
    for x in range(len(lenof_string)):
        menu_shape += '-'
    print(menu_shape)


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
# print(len(str(inventory[character_choose])))
print(f'Name: {character_choose}')
print()
print(f'Inventory:')
print_menu(inventory[character_choose])
print(f"{inventory[character_choose]}")
print_menu(inventory[character_choose])

def split_every_two_characters(s):
    return [s[i:i+2] for i in range(0, len(s), 2)]

coords = ['a', 'b', 'c', 'd', 'e', 'f']

def mapGenerator(w, h):


    for heigh in range(h):
        map_gen = {}
        map = ''

        for width in range(w):
            map += f'{width}{coords[heigh]}'
        splitted = split_every_two_characters(map)
        for x in splitted:
            monster = random.randint(1, 3)
            if monster != 3:
                map_gen.setdefault(x, ' ')
            else:
                map_gen.setdefault(x, 'M')
        print(map_gen)

mapGenerator(10, 3)

