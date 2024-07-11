

def dividedBy(num, num2):
    try:
        divnumbers = int(num / num2)
        print(f"Wynik dzielenia {divnumbers}")
    except:
        print('Podaj prawidłową liczbę. Być może próbujesz podzielić przez 0.')

dividedBy(2, 2)
dividedBy(10, 5)
dividedBy(30000, 5800)
dividedBy(2000, 0)