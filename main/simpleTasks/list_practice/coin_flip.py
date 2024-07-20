import random

num_flips = 1000
one_row = 100
list_results = []
howMany_O = 0
howMany_R = 0
streak = 0

# Drawing the results of the coin flip:
for x in range(num_flips):
    column = []
    for y in range(one_row):
        if random.randint(0, 1) == 0:
            column.append('O')
        else:
            column.append('R')
    list_results.append(column)


for row in list_results:
    eagle = 0
    headstock = 0
    print(row, end='\n')
    for cell in row:
        if cell == 'O':
            howMany_O += 1
            eagle += 1
            headstock = 0
        else:
            howMany_R += 1
            headstock += 1
            eagle = 0
        if eagle == 6 or headstock == 6:
            streak +=1


print(f"You throw eagle: {howMany_O} times")
print(f"You throw headstock: {howMany_R} times")

total_flips = howMany_O + howMany_R
def howManyPrecent(item):
    return (item / total_flips) * 100

prec_O = howManyPrecent(howMany_O)
prec_R = howManyPrecent(howMany_R)
prec_streak = howManyPrecent(streak)

print(f"The precentage result of the total throws is {round(prec_O)}% eagle and {round(prec_R)}% headstock.")
print(f"Throwing six times in a row for a total number of throws {total_flips} occured {round(prec_streak, 1)}%")