import time, os

def collatz(number):

    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        print(number)
        time.sleep(0.05)
        os.system('cls')

try:
    type_num = int(input('Add an odd number: '))
    collatz(type_num)
except:
    print('Invalid Value. Please type the number.')

