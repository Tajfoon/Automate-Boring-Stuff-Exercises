# amount_of = 0
#
# while amount_of < 5:
#     amount_of = amount_of + (2 ** 2)
#     print(f'{amount_of}')

# While with break only

# passw = 'order123'
# while True:
#     in_pass = input('Write your password: ')
#     if passw == in_pass:
#         print('You gain access. Acc balance: 100$')
#         break
#     else:
#         print('Wrong password, try again')

# While with continue
import random


while True:
    log_in = input('Wprowadz login: ')
    #continue sprawia że wracamy na początek pętli.
    if log_in != 'Jacob':
        continue
    print('Witaj Jacob!')
    passwd = input('Wprowadź hasło: ')
    if passwd != 'password123':
        continue
    print('Twoje dane są poprawne.')
    #Prosty test weryfikacji:
    ran_num = random.randint(3, 10)
    ran_num2 = random.randint(1, 5)
    ran_eq = ran_num + ran_num2
    what_number_add = int(input(f"Jaką liczbę dodać do {ran_num} żeby otrzymać {ran_eq}: "))
    if what_number_add != ran_num2:
        continue
    print('Weryfikacja zakończona sukcesem.')
    break