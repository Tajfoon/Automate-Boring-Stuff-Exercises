import pprint

birthdays = {'Jerry':'26.03.1994','Mark':'10.01.1990','Tom':'19.07.2003','Sam':'13.01.1992'}

while True:
    print('Leave blank if you want to leave.')
    name = input('Enter name: ')
    if name == '':
        break

    if name in birthdays:
        print(f"Date of birthday {name} is {birthdays[name]}")
        print(f"The key of dict is {birthdays.keys()}")
    else:
        print(f"There is no information about {name}")
        print("Enter date of birthday")
        birthD = input()
        birthdays[name] = birthD
        print('Database updated')

        # .items(), .keys(), .values()
        for k, v in birthdays.items():
            print(f"Key: {k} Value: {v}")

        # Nice look print for dictionary

        pprint.pprint(birthdays)

