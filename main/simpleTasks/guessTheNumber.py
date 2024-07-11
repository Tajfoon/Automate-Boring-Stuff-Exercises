import random

# number = random.randint(1, 20)
# print(number)
# while True:
#     guess_num = int(input('Wprowadź liczbę:'))
#     if number == guess_num:
#         print("Zgadłeś liczbę!")
#         break
#     else:
#         print('Twoja liczba jest błędna! Spróbuj ponownie.')

this_num = random.randint(1, 20)
print(this_num)
print('Zgadnij liczbe od 1, 20! Masz trzy szanse.')

for guessNum in range(1, 4):
    your_num = int(input('Wybierz liczbę: '))
    if your_num == this_num:
        print(f"Zgadłes za {guessNum} razem!")
        break
    else:
        print('Spróbuj ponownie.')



